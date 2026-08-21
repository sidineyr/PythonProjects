import pytest

from music_composer.composer import compose_melody
from music_composer.theory import scale_midi_notes


def test_melody_fills_requested_number_of_beats():
    melody = compose_melody(bars=4, beats_per_bar=4, seed=42)
    assert sum(event.duration for event in melody) == pytest.approx(16.0)


def test_generated_notes_stay_in_selected_scale():
    allowed = set(scale_midi_notes("D", "minor", 4))
    melody = compose_melody(root="D", scale="minor", octave=4, seed=7)
    assert melody
    assert all(event.note in allowed for event in melody)


def test_seed_makes_generation_reproducible():
    assert compose_melody(seed=123) == compose_melody(seed=123)


def test_invalid_randomness_is_rejected():
    with pytest.raises(ValueError):
        compose_melody(randomness=1.1)
