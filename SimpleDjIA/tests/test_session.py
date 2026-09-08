from pathlib import Path

from simple_djia.models import RankedTrack, Track
from simple_djia.profiles import get_scene
from simple_djia.session import Session


def ranked(title: str) -> RankedTrack:
    return RankedTrack(Track(Path(f"/{title}.ogg"), title), score=1.0)


def test_next_advances_until_end_without_repeating_last_track():
    session = Session(
        scene=get_scene("restaurant_piano"),
        playlist=[ranked("one"), ranked("two")],
    )

    assert session.next() == session.playlist[1]
    assert session.current_index == 1
    assert session.next() is None
    assert session.current_index == 1
