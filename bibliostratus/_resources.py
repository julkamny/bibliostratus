# bibliostratus/_resources.py
from pathlib import Path
import sys

def resource_path(rel_path: str | Path) -> str:
    """
    Return an absolute path to a bundled resource.
    - In a PyInstaller app, sys._MEIPASS points at .../Contents/Resources on macOS.
    - In dev, it falls back to this file's directory.
    """
    base = Path(getattr(sys, "_MEIPASS", Path(__file__).resolve().parent))
    return str((base / rel_path).resolve())