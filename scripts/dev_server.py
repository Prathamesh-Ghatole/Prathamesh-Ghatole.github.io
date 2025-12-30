"""Live-reload dev server.

Runs the static generator on startup and whenever inputs change, and serves the
generated ./public directory with automatic browser refresh.

Usage:
  uv run python scripts/dev_server.py

Open:
  http://localhost:8000
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

from livereload import Server


ROOT = Path(__file__).resolve().parents[1]


def build() -> None:
    """Rebuild the static site into ./public."""
    # We call the generator as a subprocess instead of importing it so this script
    # works even though ./scripts is not a Python package.
    subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "generate_site.py")],
        cwd=str(ROOT),
        check=True,
    )


def main() -> None:
    # Initial build so the first page load works.
    build()

    server = Server()

    # Rebuild on changes.
    server.watch(str(ROOT / "content"), build, delay=0.2)
    server.watch(str(ROOT / "templates"), build, delay=0.2)
    server.watch(str(ROOT / "static"), build, delay=0.2)

    # Serve output directory with livereload script injection.
    server.serve(root=str(ROOT / "public"), host="127.0.0.1", port=8000)


if __name__ == "__main__":
    main()
