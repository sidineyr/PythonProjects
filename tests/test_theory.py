import pytest

from music_composer.theory import scale_midi_notes, scale_pitch_classes


def test_c_major_pitch_classes():
    assert scale_pitch_classes("C", "major") == (0, 2, 4, 5, 7, 9, 11)


def test_a_minor_pitch_classes():
    assert scale_pitch_classes("A", "minor") == (9, 11, 0, 2, 4, 5, 7)


def test_c_major_octave_four_starts_at_middle_c():
    assert scale_midi_notes("C", "major", 4)[0] == 60


def test_invalid_root_is_rejected():
    with pytest.raises(ValueError):
        scale_pitch_classes("H", "major")
