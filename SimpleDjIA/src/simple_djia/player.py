from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import shutil
import subprocess


@dataclass(frozen=True)
class PlayerBackend:
    name: str
    executable: str
    args: tuple[str, ...]


BACKENDS = (
    PlayerBackend("mpv", "mpv", ("--no-video", "--really-quiet")),
    PlayerBackend("vlc", "cvlc", ("--play-and-exit", "--quiet")),
    PlayerBackend("ffplay", "ffplay", ("-nodisp", "-autoexit", "-loglevel", "error")),
)


def detect_backend() -> PlayerBackend | None:
    for backend in BACKENDS:
        if shutil.which(backend.executable):
            return backend
    return None


def play(path: str | Path, backend: PlayerBackend | None = None) -> subprocess.Popen:
    selected = backend or detect_backend()
    if selected is None:
        raise RuntimeError("No supported player found. Install mpv, VLC/cvlc or ffplay.")
    audio = Path(path)
    if not audio.exists():
        raise FileNotFoundError(audio)
    return subprocess.Popen([selected.executable, *selected.args, str(audio)])
