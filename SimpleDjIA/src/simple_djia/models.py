from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path


@dataclass(frozen=True)
class Track:
    path: Path
    title: str
    artist: str = "Unknown"
    genre: str = "unknown"
    bpm: float = 100.0
    energy: float = 0.5
    valence: float = 0.5
    acousticness: float = 0.5
    danceability: float = 0.5
    vocal_presence: float = 0.5
    familiarity: float = 0.5
    tags: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        for name in ("energy", "valence", "acousticness", "danceability", "vocal_presence", "familiarity"):
            value = getattr(self, name)
            if not 0.0 <= value <= 1.0:
                raise ValueError(f"{name} must be between 0 and 1")
        if not 20 <= self.bpm <= 300:
            raise ValueError("bpm must be between 20 and 300")


@dataclass(frozen=True)
class SceneProfile:
    key: str
    name: str
    description: str
    target_bpm: float
    bpm_tolerance: float
    targets: dict[str, float]
    weights: dict[str, float]
    preferred_tags: tuple[str, ...] = ()
    avoid_tags: tuple[str, ...] = ()
    max_vocal_presence: float | None = None
    transition_limit: float = 0.35


@dataclass(frozen=True)
class RankedTrack:
    track: Track
    score: float
    reasons: tuple[str, ...] = field(default_factory=tuple)
