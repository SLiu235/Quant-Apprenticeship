"""Verify the revised learning pack with the existing numerical environment."""

from datetime import datetime, timezone
from hashlib import sha256
import json
from pathlib import Path
import platform
import re
import subprocess
import sys


def main():
    root = Path(__file__).resolve().parent
    out = root / "outputs"
    logs = out / "professional_checks"
    logs.mkdir(parents=True, exist_ok=True)
    checks = [
        ("tests", ["-m", "unittest", "discover", "-s", "tests", "-v"]),
        (
            "integrated",
            [
                "-m",
                "apprentice_system.run",
                "--stage",
                "10",
                "--output",
                "outputs/integrated",
            ],
        ),
        (
            "frontier",
            ["-m", "apprentice_system.frontier", "--output", "outputs/frontier"],
        ),
        (
            "model_lab",
            ["-m", "apprentice_system.model_lab", "--output", "outputs/model_lab"],
        ),
        (
            "legacy",
            [
                "-m",
                "reference.run",
                "--project",
                "all",
                "--output",
                "outputs/legacy_check",
            ],
        ),
    ]
    results = {}
    count = None
    for name, command in checks:
        proc = subprocess.run(
            [sys.executable, *command], cwd=root, capture_output=True, text=True
        )
        text = proc.stdout + proc.stderr
        (logs / f"{name}.log").write_text(text)
        if proc.returncode:
            raise RuntimeError(f"{name} failed; see {logs / (name + '.log')}: {text}")
        results[name] = "passed"
        if name == "tests":
            count = int(re.search(r"Ran (\d+) tests", text).group(1))
    bad, link_count, document_count = [], 0, 0
    for path in root.rglob("*.md"):
        if any(
            part in {"submissions", "deliverables", ".venv", ".git"}
            for part in path.relative_to(root).parts
        ):
            continue
        document_count += 1
        for target in re.findall(r"\]\(([^)]+)\)", path.read_text()):
            if re.match(r"(https?://|#|mailto:)", target):
                continue
            target = target.split("#")[0].strip("<>")
            resolved = (path.parent / target).resolve()
            if resolved == out / "professional_verification.json":
                continue
            link_count += 1
            if not resolved.exists():
                bad.append(f"{path.relative_to(root)} -> {target}")
    if bad:
        raise RuntimeError("Broken local links: " + repr(bad))
    sources = sorted((root / "apprentice_system").glob("*.py")) + sorted(
        (root / "tests").glob("*.py")
    )
    report = dict(
        verified_at_utc=datetime.now(timezone.utc).isoformat(),
        python=platform.python_version(),
        commands=checks,
        checks=results,
        tests_passed=count,
        documents_checked=document_count,
        local_links_checked=link_count,
        broken_links=0,
        implemented=dict(
            foundation_stages=10,
            professional_studios=6,
            economic_scenarios=18,
            real_data_model_procedures=5,
            existing_worked_projects=8,
        ),
        source_hashes={
            str(p.relative_to(root)): sha256(p.read_bytes()).hexdigest()
            for p in sources
        },
        scope="Package/software evidence only. Real model training on inspected snapshots; synthetic economics; authored AI-output cases. No live model, prospective alpha, brokerage or learner-competency claim.",
    )
    (out / "professional_verification.json").write_text(
        json.dumps(report, indent=2) + "\n"
    )
    print(
        json.dumps(
            {k: v for k, v in report.items() if k not in {"source_hashes", "commands"}},
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
