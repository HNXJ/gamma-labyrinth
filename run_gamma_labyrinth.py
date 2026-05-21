"""Compatibility launcher for the local Gamma Labyrinth control server."""

import sys
from pathlib import Path

repo_root = Path(__file__).resolve().parent
src_root = repo_root / "src"
if str(src_root) not in sys.path:
    sys.path.insert(0, str(src_root))

from gamma_labyrinth.server import main

if __name__ == "__main__":
    raise SystemExit(main())
