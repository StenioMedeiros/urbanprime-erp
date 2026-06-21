import subprocess
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]


def main() -> None:
    raise SystemExit(subprocess.call([sys.executable, "-m", "streamlit", "run", "src/ui/app.py"], cwd=ROOT_DIR))


if __name__ == "__main__":
    main()
