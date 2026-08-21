"""Harmony helpers: diatonic triads, progressions, chords and bass."""

from dataclasses import dataclass

from .theory import scale_midi_notes

PROGRESSIONS = {
    "I-IV-V-I": (1, 4, 5, 1),
    "I-V-vi-IV": (1, 5, 6, 4),
    "ii-V-I-I": (2, 5, 1, 1),
    "I-vi-IV-V": (1, 6, 4, 5),
}


@dataclass(frozen=True)
class ChordEvent:
    notes: tuple[int, int, int]
    start: float
    duration: float
    velocity: int = 58


@dataclass(frozen=True)
class BassEvent:
    note: int
    start: float
    duration: float
    velocity: int = 72


def diatonic_triad(root: str, scale: str, octave: int, degree: int) -> tuple[int, int, int]:
    """Return a scale-built triad for degree 1..7."""
    if not 1 <= degree <= 7:
        raise ValueError("degree must be between 1 and 7")
    base = scale_midi_notes(root, scale, octave)
    extended = base + [note + 12 for note in base]
    index = degree - 1
    return (extended[index], extended[index + 2], extended[index + 4])


def progression_degrees(name: str) -> tuple[int, ...]:
    if name not in PROGRESSIONS:
        raise ValueError(f"Unknown progression: {name}")
    return PROGRESSIONS[name]


def chord_for_bar(root: str, scale: str, octave: int, progression: str, bar: int) -> tuple[int, int, int]:
    degrees = progression_degrees(progression)
    degree = degrees[bar % len(degrees)]
    return diatonic_triad(root, scale, octave, degree)


def build_accompaniment(
    root: str,
    scale: str,
    bars: int,
    beats_per_bar: int,
    progression: str,
    chord_octave: int = 3,
    bass_octave: int = 2,
) -> tuple[list[ChordEvent], list[BassEvent]]:
    """Create one sustained triad and a root/fifth bass pattern per bar."""
    chords: list[ChordEvent] = []
    bass: list[BassEvent] = []

    for bar in range(bars):
        start = float(bar * beats_per_bar)
        triad = chord_for_bar(root, scale, chord_octave, progression, bar)
        chords.append(ChordEvent(triad, start, float(beats_per_bar)))

        bass_triad = chord_for_bar(root, scale, bass_octave, progression, bar)
        root_note, _, fifth = bass_triad
        if beats_per_bar >= 4:
            bass.append(BassEvent(root_note, start, 2.0))
            bass.append(BassEvent(fifth, start + 2.0, float(beats_per_bar - 2)))
        else:
            bass.append(BassEvent(root_note, start, 1.0))
            bass.append(BassEvent(fifth, start + 1.0, float(beats_per_bar - 1)))

    return chords, bass
