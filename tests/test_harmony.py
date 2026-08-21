from music_composer.harmony import build_accompaniment, diatonic_triad, progression_degrees


def test_c_major_tonic_triad():
    assert diatonic_triad("C", "major", 4, 1) == (60, 64, 67)


def test_pop_progression_degrees():
    assert progression_degrees("I-V-vi-IV") == (1, 5, 6, 4)


def test_accompaniment_creates_one_chord_per_bar():
    chords, bass = build_accompaniment("C", "major", 8, 4, "I-V-vi-IV")
    assert len(chords) == 8
    assert len(bass) == 16


def test_progression_repeats_across_bars():
    chords, _ = build_accompaniment("C", "major", 5, 4, "I-IV-V-I")
    assert chords[0].notes == chords[3].notes == chords[4].notes
