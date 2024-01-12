import mido
import random

def generate_random_notes(num_notes):
    notes = []
    for _ in range(num_notes):
        note_number = 60  # Altura da nota, 60 é a nota central do piano (C4)
        velocity = random.randint(80, 100)
        duration = 0.4
        notes.append({'note': note_number, 'velocity': velocity, 'duration': duration})
    return notes

def create_midi_file(output_file, notes):
    mid = mido.MidiFile()
    track = mido.MidiTrack()

    for note in notes:
        track.append(mido.Message('note_on', note=note['note'], velocity=note['velocity'], time=0))
        track.append(mido.Message('note_off', note=note['note'], velocity=note['velocity'], time=int(note['duration'] * 480)))  # 480 ticks per beat

    mid.tracks.append(track)
    mid.save(output_file)

if __name__ == "__main__":
    num_notes = 50
    output_file = "random_notes.mid"

    random_notes = generate_random_notes(num_notes)
    create_midi_file(output_file, random_notes)

    print(f"MIDI file '{output_file}' created successfully.")
