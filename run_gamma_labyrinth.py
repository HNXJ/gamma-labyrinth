import os
import sys
from pathlib import Path

# Resolve workspace root: assuming repository structure of repos/
# D:\workspace\gemini-gamma-labyrinth\repos\gamma-labyrinth -> D:\workspace\gemini-gamma-labyrinth
repo_root = Path(__file__).resolve().parent.parent
workspace_root = repo_root.parent
gamma_src = repo_root / "gamma" / "src"

sys.path.insert(0, str(gamma_src))

from gamma_runtime.launcher import main

if __name__ == "__main__":
    main()
