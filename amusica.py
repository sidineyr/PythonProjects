import mido
import random

# Definir duração da música em segundos
duration = 120

# Definir tempo de uma nota ou silêncio
note_duration = 0.6
rest_duration = 0.09

# Definir a resolução da nota (quanto menor, mais precisa)
resolution = 32

# Converter o tempo de nota/silêncio em unidades de tempo do MIDI
note_ticks = int(note_duration * resolution)
rest_ticks = int(rest_duration * resolution)

# Criar um objeto MIDI com um canal e tempo inicial
mid = mido.MidiFile()
track = mido.MidiTrack()
mid.tracks.append(track)
track.append(mido.Message('program_change', program=0, time=0))

# Definir tempo inicial
time = 0

# Gerar notas e silêncios aleatórios
while time < duration * resolution:
    # Gerar nota aleatória ou silêncio
    if random.random() < 0.5:
        # Gerar nota aleatória
        note_value = random.randint(40, 90)
        track.append(mido.Message('note_on', note=note_value, velocity=127, time=time))
        time = note_ticks
        track.append(mido.Message('note_off', note=note_value, velocity=127, time=time))
    else:
        # Gerar silêncio
        time = rest_ticks

# Salvar o arquivo de música MIDI em disco
mid.save('minha_musica_.mid')


