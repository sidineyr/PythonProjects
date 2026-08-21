"""Rule-based, harmony-aware melody generation."""

from dataclasses import dataclass
import random

from .harmony import chord_for_bar
from .theory import scale_midi_notes


@dataclass(frozen=True)
class MelodyEvent:
    note: int
    start: float
    duration: float
    velocity: int


def compose_melody(
    root: str = "C",
    scale: str = "major",
    octave: int = 4,
    bars: int = 4,
    beats_per_bar: int = 4,
    randomness: float = 0.5,
    seed: int | None = None,
    progression: str | None = None,
) -> list[MelodyEvent]:
    """Generate a melody constrained to a scale and optionally its harmony."""
    if bars < 1 or beats_per_bar < 1:
        raise ValueError("bars and beats_per_bar must be positive")
    if not 0 <= randomness <= 1:
        raise ValueError("randomness must be between 0 and 1")

    rng = random.Random(seed)
    notes = scale_midi_notes(root, scale, octave)
    durations = (0.5, 1.0, 2.0)
    total_beats = float(bars * beats_per_bar)
    events: list[MelodyEvent] = []
    cursor = 0.0
    previous = notes[0]

    while cursor < total_beats:
        remaining = total_beats - cursor
        allowed = [duration for duration in durations if duration <= remaining]
        duration = rng.choice(allowed)
        bar = min(int(cursor // beats_per_bar), bars - 1)
        beat_in_bar = cursor % beats_per_bar

        candidates = notes
        if progression and beat_in_bar in (0.0, 2.0):
            chord = chord_for_bar(root, scale, octave, progression, bar)
            chord_pcs = {note % 12 for note in chord}
            harmonic = [note for note in notes if note % 12 in chord_pcs]
            if harmonic:
                candidates = harmonic

        if rng.random() < randomness:
            note = rng.choice(candidates)
        else:
            nearest = min(candidates, key=lambda candidate: abs(candidate - previous))
            index = candidates.index(nearest)
            step = rng.choice((-1, 0, 1))
            note = candidates[max(0, min(len(candidates) - 1, index + step))]

        velocity = rng.randint(72, 100)
        events.append(MelodyEvent(note, cursor, duration, velocity))
        previous = note
        cursor += duration

    return events
