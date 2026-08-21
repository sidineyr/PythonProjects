"""MIDI export helpers."""

from pathlib import Path
from midiutil import MIDIFile

from .composer import MelodyEvent


def write_midi(
    events: list[MelodyEvent],
    filename: str | Path,
    tempo: int = 120,
    instrument: int = 0,
) -> Path:
    """Write melody events to a standard MIDI file."""
    if not 20 <= tempo <= 300:
        raise ValueError("tempo must be between 20 and 300 BPM")
    if not 0 <= instrument <= 127:
        raise ValueError("instrument must be a General MIDI program (0-127)")

    path = Path(filename)
    midi = MIDIFile(1)
    midi.addTempo(0, 0, tempo)
    midi.addProgramChange(0, 0, 0, instrument)

    for event in events:
        midi.addNote(0, 0, event.note, event.start, event.duration, event.velocity)

    with path.open("wb") as output:
        midi.writeFile(output)
    return path
