"""Multi-track MIDI export helpers."""

from pathlib import Path
from midiutil import MIDIFile

from .composer import MelodyEvent
from .harmony import BassEvent, ChordEvent


def write_midi(
    events: list[MelodyEvent],
    filename: str | Path,
    tempo: int = 120,
    instrument: int = 0,
    chords: list[ChordEvent] | None = None,
    bass: list[BassEvent] | None = None,
    beats_per_bar: int = 4,
    chord_instrument: int = 48,
    bass_instrument: int = 32,
) -> Path:
    """Write melody plus optional harmony and bass to a multi-track MIDI file."""
    if not 20 <= tempo <= 300:
        raise ValueError("tempo must be between 20 and 300 BPM")
    for program in (instrument, chord_instrument, bass_instrument):
        if not 0 <= program <= 127:
            raise ValueError("instruments must be General MIDI programs (0-127)")
    if beats_per_bar not in (2, 3, 4):
        raise ValueError("beats_per_bar must be 2, 3 or 4")

    path = Path(filename)
    midi = MIDIFile(3)
    midi.addTempo(0, 0, tempo)
    midi.addTimeSignature(0, 0, beats_per_bar, 2, 24)
    midi.addTrackName(0, 0, "Melody")
    midi.addTrackName(1, 0, "Harmony")
    midi.addTrackName(2, 0, "Bass")
    midi.addProgramChange(0, 0, 0, instrument)
    midi.addProgramChange(1, 1, 0, chord_instrument)
    midi.addProgramChange(2, 2, 0, bass_instrument)

    for event in events:
        midi.addNote(0, 0, event.note, event.start, event.duration, event.velocity)

    for event in chords or []:
        for note in event.notes:
            midi.addNote(1, 1, note, event.start, event.duration, event.velocity)

    for event in bass or []:
        midi.addNote(2, 2, event.note, event.start, event.duration, event.velocity)

    with path.open("wb") as output:
        midi.writeFile(output)
    return path
