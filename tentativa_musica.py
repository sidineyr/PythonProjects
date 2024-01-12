import mido
import random

def generate_random_notes(num_notes_per_pitch, pitches):
    notes = []
    for pitch in pitches:
        for _ in range(num_notes_per_pitch):
            velocity = random.randint(100, 127)
            duration = 0.4
            notes.append({'note': pitch, 'velocity': velocity, 'duration': duration})

    return notes

def generate_silence(num_silence):
    silence = []
    for _ in range(num_silence):
        silence_duration = 0.2
        silence.append({'note': None, 'velocity': 0, 'duration': silence_duration})
    return silence

def create_midi_file(output_file, notes):
    mid = mido.MidiFile()
    track = mido.MidiTrack()

    for note in notes:
        if note['note'] is not None:
            track.append(mido.Message('note_on', note=note['note'], velocity=note['velocity'], time=0))
            track.append(mido.Message('note_off', note=note['note'], velocity=note['velocity'], time=int(note['duration'] * 480)))  # 480 ticks per beat
        else:
            track.append(mido.Message('note_on', note=60, velocity=0, time=int(note['duration'] * 480)))  # Add silence

    mid.tracks.append(track)
    mid.save(output_file)

if __name__ == "__main__":
    num_notes_per_pitch = 7
    num_silence = 50 - (num_notes_per_pitch * 4)  # Preencha com silêncios para completar 50 notas
    pitches = [60, 62, 64, 65, 67, 69, 71]  # Dó, Si, Ré, Fá
    output_file = "random_notes.mid"

    random_notes = generate_random_notes(num_notes_per_pitch, pitches)
    silence = generate_silence(num_silence)

    mixed_notes = random_notes + silence
    random.shuffle(mixed_notes)  # Embaralhe a ordem das notas

    create_midi_file(output_file, mixed_notes)

    print(f"MIDI file '{output_file}' created successfully.")
