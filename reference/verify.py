"""Course release verification: structure, links, fresh executions, tests, provenance.
Run: python -m reference.verify
"""

import json
import platform
import re
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path
import numpy as np
import scipy
from .common import COURSE, DATA, digest
from .run import MODULES


def compare(recorded, fresh, path=""):
    # Timings are actual measurements and must never be asserted identical.
    if path in ("/loop", "/vectorized", "/runtime_python", "/cpu", "/numpy"):
        return
    if isinstance(recorded, dict):
        if set(recorded) != set(fresh):
            raise AssertionError(f"key mismatch at {path}")
        for key in recorded:
            compare(recorded[key], fresh[key], path + "/" + key)
    elif isinstance(recorded, list):
        if len(recorded) != len(fresh):
            raise AssertionError(f"length mismatch at {path}")
        for index, (a, b) in enumerate(zip(recorded, fresh)):
            compare(a, b, path + f"/{index}")
    elif isinstance(recorded, (int, float)) and not isinstance(recorded, bool):
        if not np.isclose(recorded, fresh, atol=1e-8, rtol=1e-7):
            raise AssertionError(f"numerical mismatch at {path}: {recorded}, {fresh}")
    elif recorded != fresh:
        raise AssertionError(f"value mismatch at {path}")


def main():
    lessons = sorted((COURSE / "lessons").glob("*.md"))
    keys = sorted((COURSE / "answers").glob("*.md"))
    assert len(lessons) == len(keys) == 24
    assert [p.name for p in lessons] == [p.name for p in keys]
    assignments = 0
    for lesson, key in zip(lessons, keys):
        text, answer = lesson.read_text(), key.read_text()
        for label in ("A1", "A2", "A3"):
            assert f"**{label}.**" in text, (lesson, label)
            assert f"## {label}" in answer, (key, label)
            assignments += 1
        assert "Prerequisites:" in text and "Suggested effort:" in text
        assert "## Lab procedure" in text and "Mastery check:" in text
        assert "## Worked" in text
        assert len(text.split()) >= 400 and len(answer.split()) >= 150
    for number, module in enumerate(MODULES, 1):
        assert (COURSE / "reference" / f"{module}.py").exists()
        matches = [
            p
            for p in (COURSE / "projects").glob(f"{number:02}_*.md")
            if p.name != "08_worked_memo.md"
        ]
        assert len(matches) == 1
        project = matches[0].read_text()
        assert (
            "## Student deliverables" in project
            and "## Acceptance and answer guidance" in project
        )
        assert len(project.split()) >= 350
    local_links = 0
    for path in COURSE.rglob("*.md"):
        if "submissions" in path.relative_to(COURSE).parts:
            continue
        for target in re.findall(r"\]\(([^)]+)\)", path.read_text()):
            if re.match(r"(https?://|#|mailto:)", target):
                continue
            target = target.split("#")[0].strip("<>")
            resolved = (path.parent / target).resolve()
            if resolved == COURSE / "outputs/verification.json":
                continue  # This file is created by the successful check.
            assert (
                resolved.exists()
            ), f"broken link: {path.relative_to(COURSE)} -> {target}"
            local_links += 1
    with tempfile.TemporaryDirectory(prefix="quant-course-") as directory:
        run = subprocess.run(
            [
                sys.executable,
                "-m",
                "reference.run",
                "--project",
                "all",
                "--output",
                directory,
            ],
            cwd=COURSE,
            text=True,
            capture_output=True,
        )
        (COURSE / "outputs/fresh_run.log").write_text(run.stdout + run.stderr)
        assert run.returncode == 0, run.stderr
        for module in MODULES:
            recorded = json.loads((COURSE / "outputs" / f"{module}.json").read_text())
            fresh = json.loads((Path(directory) / f"{module}.json").read_text())
            compare(recorded, fresh)
    tests = subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"],
        cwd=COURSE,
        text=True,
        capture_output=True,
    )
    (COURSE / "outputs/tests.log").write_text(tests.stdout + tests.stderr)
    assert tests.returncode == 0, tests.stderr
    count = int(re.search(r"Ran (\d+) tests", tests.stderr).group(1))
    source_paths = [
        DATA / "results/reddit_recent_2026/predictions.csv",
        DATA / "behavior_irl/mdp.py",
        DATA / "behavior_irl/models.py",
    ] + sorted((DATA / "real_data/recent_prices").glob("*.json"))
    code_paths = sorted((COURSE / "reference").glob("*.py")) + sorted(
        (COURSE / "tests").glob("*.py")
    )
    result = {
        "status": "passed",
        "verified_at_utc": datetime.now(timezone.utc).isoformat(),
        "python": platform.python_version(),
        "numpy": np.__version__,
        "scipy": scipy.__version__,
        "lessons": len(lessons),
        "answer_keys": len(keys),
        "matched_assignments": assignments,
        "worked_projects_executed": len(MODULES),
        "unit_tests_passed": count,
        "local_links_checked": local_links,
        "deterministic_outputs_match": True,
        "timing_fields_excluded_from_exact_comparison": True,
        "source_hashes": {
            str(p.relative_to(COURSE.parent)): digest(p) for p in source_paths
        },
        "code_hashes": {str(p.relative_to(COURSE)): digest(p) for p in code_paths},
        "scope": "Offline local references; no new social feed, live LLM, GPU or brokerage execution. Automated structure/link checks supplement the documented editorial review; they do not certify pedagogy or market validity.",
    }
    (COURSE / "outputs/verification.json").write_text(
        json.dumps(result, indent=2) + "\n"
    )
    print(
        json.dumps(
            {k: v for k, v in result.items() if not k.endswith("_hashes")}, indent=2
        )
    )


if __name__ == "__main__":
    main()
