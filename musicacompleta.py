import random
import mido

# Define as configurações da música
total_time = 120  # tempo total em segundos (2 minutos)
num_notes = 240  # número total de notas
prelude_time = 30  # tempo do prelúdio em segundos
interlude_time = 60  # tempo do interlúdio em segundos
postlude_time = 30  # tempo do pós-lúdio em segundos
note_duration = 0.9  # duração de cada nota em segundos
note_volume = 100  # volume de cada nota

# Cria um novo arquivo MIDI
midi_file = mido.MidiFile()
track = mido.MidiTrack()
midi_file.tracks.append(track)

# Adiciona notas aleatórias ao longo da música
time_per_note = total_time / num_notes
for i in range(num_notes):
    # Define o tempo da nota
    if i < num_notes * prelude_time / total_time:
        time = random.uniform(i * time_per_note, (i+1) * time_per_note)
    elif i >= num_notes * (total_time - postlude_time) / total_time:
        time = random.uniform((i-1) * time_per_note, i * time_per_note)
    else:
        time = random.uniform((i-1) * time_per_note, (i+1) * time_per_note)

    # Cria uma nota aleatória ou um silêncio
    if random.random() < 0.5:
        note = random.randint(40, 80)
        velocity = note_volume
        track.append(mido.Message('note_on', note=note, velocity=velocity, time=int(time*1000)))
        track.append(mido.Message('note_off', note=note, velocity=velocity, time=int(note_duration*1000)))
    else:
        track.append(mido.Message('note_on', note=60, velocity=0, time=int(time*1000)))
        track.append(mido.Message('note_off', note=60, velocity=0, time=int(note_duration*1000)))

# Salva o arquivo MIDI
midi_file.save('musica.mid')
