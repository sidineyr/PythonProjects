import random
import mido

# Configurações iniciais do arquivo MIDI
midi_file = mido.MidiFile(type=0)
track = mido.MidiTrack()
midi_file.tracks.append(track)
track.append(mido.Message('program_change', program=1, time=0))

# Definindo as notas musicais
notes = ['C3', 'D3', 'E3', 'F3', 'G3', 'A3', 'B3']

# Loop para gerar 120 notas aleatórias
for i in range(120):
    note = random.choice(notes)
    velocity = 100  # Volume
    duration = 0.15 # Tempo de execução para cada nota
    time = mido.second2tick(duration, ticks_per_beat=midi_file.ticks_per_beat, tempo=midi_file.tracks[0][0].tempo)
    track.append(mido.Message('note_on', note=mido.note_name_to_number(note), velocity=velocity, time=0))
    track.append(mido.Message('note_off', note=mido.note_name_to_number(note), velocity=velocity, time=time))

# Salvando o arquivo MIDI
midi_file.save('meuarquivo.mid')
