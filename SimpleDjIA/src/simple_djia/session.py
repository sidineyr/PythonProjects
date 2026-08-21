from __future__ import annotations

from dataclasses import dataclass
import time

from .models import RankedTrack, SceneProfile, Track
from .player import play
from .selector import build_playlist


@dataclass
class Session:
    scene: SceneProfile
    playlist: list[RankedTrack]
    current_index: int = 0

    @property
    def current(self) -> RankedTrack | None:
        if not self.playlist:
            return None
        return self.playlist[self.current_index]

    def next(self) -> RankedTrack | None:
        if self.current_index + 1 >= len(self.playlist):
            return None
        self.current_index += 1
        return self.current


def create_session(tracks: list[Track], scene: SceneProfile, limit: int = 20) -> Session:
    return Session(scene=scene, playlist=build_playlist(tracks, scene, limit))


def play_session(session: Session) -> None:
    """Play the curated list sequentially with the detected open-source backend."""
    for index, ranked in enumerate(session.playlist):
        session.current_index = index
        process = play(ranked.track.path)
        while process.poll() is None:
            time.sleep(0.25)
