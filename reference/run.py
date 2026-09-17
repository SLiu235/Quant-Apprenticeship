import argparse, importlib, json, platform
from pathlib import Path
from .common import COURSE

MODULES = [
    "p01_audit",
    "p02_replay",
    "p03_baseline",
    "p04_text",
    "p05_risk",
    "p06_irl",
    "p07_operations",
    "p08_committee",
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--project", choices=["all"] + [str(i) for i in range(1, 9)], default="all"
    )
    parser.add_argument("--output", type=Path, default=COURSE / "outputs")
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    chosen = MODULES if args.project == "all" else [MODULES[int(args.project) - 1]]
    for name in chosen:
        result = importlib.import_module("reference." + name).run()
        result["runtime_python"] = platform.python_version()
        path = args.output / (name + ".json")
        path.write_text(json.dumps(result, indent=2, allow_nan=False) + "\n")
        print(f"{name}: {path}")


if __name__ == "__main__":
    main()
