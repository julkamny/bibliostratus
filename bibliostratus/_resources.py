# bibliostratus/_resources.py
from __future__ import annotations

from pathlib import Path
import sys


def _base_path() -> Path:
    """Return the root directory for bundled resources."""
    meipass = getattr(sys, "_MEIPASS", None)
    if meipass:
        return Path(meipass)
    return Path(__file__).resolve().parent


def resource_path(rel_path: str | Path) -> str:
    """Return an absolute path to a bundled resource.

    The helper mirrors PyInstaller's runtime layout so a single code path works
    both in development (when files live next to the sources) and once bundled
    (where they reside under ``sys._MEIPASS``). Absolute inputs are returned as-is
    to keep compatibility with user-provided locations.
    """

    rel_path = Path(rel_path)
    if rel_path.is_absolute():
        return str(rel_path)
    return str((_base_path() / rel_path).resolve())
