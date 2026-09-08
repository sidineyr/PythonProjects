from __future__ import annotations

import json
from pathlib import Path

from .models import Track


def load_library(path: str | Path) -> list[Track]:
    source = Path(path)
    data = json.loads(source.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError("library JSON must contain a list")
    tracks: list[Track] = []
    for item in data:
        raw_path = Path(item["path"]).expanduser()
        if not raw_path.is_absolute():
            raw_path = (source.parent / raw_path).resolve()
        tracks.append(Track(
            path=raw_path,
            title=item.get("title", raw_path.stem),
            artist=item.get("artist", "Unknown"),
            genre=item.get("genre", "unknown"),
            bpm=float(item.get("bpm", 100)),
            energy=float(item.get("energy", 0.5)),
            valence=float(item.get("valence", 0.5)),
            acousticness=float(item.get("acousticness", 0.5)),
            danceability=float(item.get("danceability", 0.5)),
            vocal_presence=float(item.get("vocal_presence", 0.5)),
            familiarity=float(item.get("familiarity", 0.5)),
            tags=tuple(item.get("tags", [])),
        ))
    return tracks
