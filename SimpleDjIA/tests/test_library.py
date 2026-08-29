import json

from simple_djia.library import load_library


def test_load_library_resolves_relative_paths(tmp_path):
    data = [{
        "path": "music/a.ogg",
        "title": "A",
        "artist": "Artist",
        "bpm": 90,
        "energy": 0.4,
        "valence": 0.5,
        "acousticness": 0.6,
        "danceability": 0.3,
        "vocal_presence": 0.1,
        "familiarity": 0.4,
        "tags": ["piano"]
    }]
    source = tmp_path / "library.json"
    source.write_text(json.dumps(data), encoding="utf-8")
    tracks = load_library(source)
    assert tracks[0].path == (tmp_path / "music/a.ogg").resolve()
    assert tracks[0].tags == ("piano",)


def test_library_must_be_list(tmp_path):
    source = tmp_path / "library.json"
    source.write_text("{}", encoding="utf-8")
    try:
        load_library(source)
    except ValueError as exc:
        assert "list" in str(exc)
    else:
        raise AssertionError("expected ValueError")
