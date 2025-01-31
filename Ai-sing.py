import tkinter as tk
from tkinter import ttk, messagebox
import mido
from mido import MidiFile, MidiTrack, Message
import random

# Constants
NOTE_NAMES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
DURATIONS = [0.25, 0.5, 1, 2]  # Quarter, half, whole, double notes
TIME_SIGNATURES = ['4/4', '3/4', '2/4']
TEMPO = 500000  # Default tempo (microseconds per beat)

# Helper functions
def note_name_to_midi(note_name, octave=4):
    """Convert a note name (e.g., 'C#') to a MIDI note number."""
    return NOTE_NAMES.index(note_name) + 12 * (octave + 1)

def generate_random_note():
    """Generate a random note and duration."""
    note = random.choice(NOTE_NAMES)
    duration = random.choice(DURATIONS)
    return note, duration

def create_midi_file(rules, filename):
    """Create a MIDI file based on the given rules."""
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)

    # Set tempo
    track.append(mido.MetaMessage('set_tempo', tempo=TEMPO))

    # Add notes based on rules
    for _ in range(rules['num_notes']):
        note, duration = generate_random_note() if rules['randomize'] else (rules['note'], rules['duration'])
        midi_note = note_name_to_midi(note, rules['octave'])
        velocity = 64  # Default velocity

        # Note on
        track.append(Message('note_on', note=midi_note, velocity=velocity, time=0))
        # Note off
        track.append(Message('note_off', note=midi_note, velocity=velocity, time=int(duration * 480)))

    # Save MIDI file
    mid.save(filename)
    messagebox.showinfo("Success", f"MIDI file saved as {filename}")

# GUI Application
class MidiComposerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MIDI Composer")

        # Variables
        self.rules = {
            'num_notes': tk.IntVar(value=10),
            'note': tk.StringVar(value='C'),
            'duration': tk.DoubleVar(value=1.0),
            'octave': tk.IntVar(value=4),
            'randomize': tk.BooleanVar(value=False),
            'time_signature': tk.StringVar(value='4/4'),
        }

        # GUI Layout
        ttk.Label(root, text="Number of Notes:").grid(row=0, column=0, padx=10, pady=5)
        ttk.Entry(root, textvariable=self.rules['num_notes']).grid(row=0, column=1, padx=10, pady=5)

        ttk.Label(root, text="Note:").grid(row=1, column=0, padx=10, pady=5)
        ttk.Combobox(root, textvariable=self.rules['note'], values=NOTE_NAMES).grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(root, text="Duration:").grid(row=2, column=0, padx=10, pady=5)
        ttk.Combobox(root, textvariable=self.rules['duration'], values=DURATIONS).grid(row=2, column=1, padx=10, pady=5)

        ttk.Label(root, text="Octave:").grid(row=3, column=0, padx=10, pady=5)
        ttk.Entry(root, textvariable=self.rules['octave']).grid(row=3, column=1, padx=10, pady=5)

        ttk.Label(root, text="Time Signature:").grid(row=4, column=0, padx=10, pady=5)
        ttk.Combobox(root, textvariable=self.rules['time_signature'], values=TIME_SIGNATURES).grid(row=4, column=1, padx=10, pady=5)

        ttk.Checkbutton(root, text="Randomize Notes and Durations", variable=self.rules['randomize']).grid(row=5, column=0, columnspan=2, pady=5)

        ttk.Button(root, text="Create Jingle", command=lambda: self.create_midi('jingle.mid')).grid(row=6, column=0, pady=10)
        ttk.Button(root, text="Create Intro", command=lambda: self.create_midi('intro.mid')).grid(row=6, column=1, pady=10)
        ttk.Button(root, text="Create Stinger", command=lambda: self.create_midi('stinger.mid')).grid(row=7, column=0, columnspan=2, pady=10)

    def create_midi(self, filename):
        """Create a MIDI file based on the current rules."""
        rules = {key: var.get() for key, var in self.rules.items()}
        create_midi_file(rules, filename)

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = MidiComposerApp(root)
    root.mainloop()
