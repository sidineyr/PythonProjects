"""Small music-theory helpers used by the composer."""

NOTE_TO_PC = {
    "C": 0, "C#": 1, "D": 2, "D#": 3, "E": 4, "F": 5,
    "F#": 6, "G": 7, "G#": 8, "A": 9, "A#": 10, "B": 11,
}

SCALES = {
    "major": (0, 2, 4, 5, 7, 9, 11),
    "minor": (0, 2, 3, 5, 7, 8, 10),
}


def scale_pitch_classes(root: str, scale: str = "major") -> tuple[int, ...]:
    """Return pitch classes (0-11) for a major or natural-minor scale."""
    root = root.upper()
    if root not in NOTE_TO_PC:
        raise ValueError(f"Unknown root note: {root}")
    if scale not in SCALES:
        raise ValueError(f"Unknown scale: {scale}")
    base = NOTE_TO_PC[root]
    return tuple((base + interval) % 12 for interval in SCALES[scale])


def scale_midi_notes(root: str, scale: str, octave: int) -> list[int]:
    """Build one octave of MIDI notes for the selected scale."""
    if not 0 <= octave <= 8:
        raise ValueError("Octave must be between 0 and 8")
    root_pc = NOTE_TO_PC.get(root.upper())
    if root_pc is None:
        raise ValueError(f"Unknown root note: {root}")
    root_midi = 12 * (octave + 1) + root_pc
    notes = [root_midi + interval for interval in SCALES[scale]]
    return [note for note in notes if 0 <= note <= 127]
