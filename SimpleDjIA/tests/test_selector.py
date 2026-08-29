from pathlib import Path

import pytest

from simple_djia.models import Track
from simple_djia.profiles import get_scene
from simple_djia.selector import build_playlist, score_track


def track(title, artist, bpm, energy, danceability, acousticness=0.5, valence=0.5, vocals=0.1, tags=()):
    return Track(Path(f"/{title}.ogg"), title, artist, bpm=bpm, energy=energy,
                 danceability=danceability, acousticness=acousticness,
                 valence=valence, vocal_presence=vocals, familiarity=0.5, tags=tags)


def test_restaurant_prefers_acoustic_piano():
    scene = get_scene("restaurant_piano")
    piano = track("piano", "A", 80, 0.28, 0.2, 0.95, 0.6, tags=("piano", "instrumental"))
    club = track("club", "B", 128, 0.95, 0.95, 0.05, 0.8, tags=("house", "party"))
    assert score_track(piano, scene).score > score_track(club, scene).score


def test_avoid_tag_blocks_track():
    scene = get_scene("calm_connection")
    harsh = track("harsh", "A", 72, 0.2, 0.1, tags=("harsh",))
    assert score_track(harsh, scene).score < -900


def test_playlist_avoids_same_artist_when_alternative_exists():
    scene = get_scene("mega_party_dj")
    tracks = [
        track("one", "DJ A", 126, 0.9, 0.95, 0.1, 0.8, tags=("house",)),
        track("two", "DJ A", 125, 0.88, 0.94, 0.1, 0.8, tags=("house",)),
        track("three", "DJ B", 124, 0.86, 0.92, 0.1, 0.8, tags=("house",)),
    ]
    playlist = build_playlist(tracks, scene, 3)
    assert playlist[0].track.artist != playlist[1].track.artist


@pytest.mark.parametrize("limit", [0, -1])
def test_playlist_rejects_non_positive_limit(limit):
    scene = get_scene("restaurant_piano")
    tracks = [track("one", "A", 82, 0.3, 0.2, 0.9, 0.6, tags=("piano",))]
    with pytest.raises(ValueError, match="at least 1"):
        build_playlist(tracks, scene, limit)
