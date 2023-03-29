import random
import mido

# Definindo as constantes
BPM = 120
TEMPO_PRELUDIO = 30  # segundos
TEMPO_INTERLUDIO = 60  # segundos
TEMPO_POSLUDIO = 30  # segundos
NOTAS_TOTAL = 480
DURACAO_NOTAS = 0.9  # segundos
VOLUME = 100

# Calculando o número de notas e silêncios em cada parte da música
NOTAS_PRELUDIO = int(NOTAS_TOTAL * (TEMPO_PRELUDIO / 120))
NOTAS_INTERLUDIO = int(NOTAS_TOTAL * (TEMPO_INTERLUDIO / 120))
NOTAS_POSLUDIO = NOTAS_TOTAL - NOTAS_PRELUDIO - NOTAS_INTERLUDIO

# Criando uma lista com as notas e silêncios
notas = []
for i in range(NOTAS_TOTAL):
    if i < NOTAS_PRELUDIO:
        # notas aleatórias no prelúdio
        notas.append(random.randint(50, 90))
    elif i < NOTAS_PRELUDIO + NOTAS_INTERLUDIO:
        # silêncios no interlúdio
        notas.append(None)
    else:
        # notas aleatórias no poslúdio
        notas.append(random.randint(50, 90))

# Criando o objeto MIDI
mid = mido.MidiFile()
track = mido.MidiTrack()
mid.tracks.append(track)

# Definindo o tempo da música
tick_per_beat = mid.ticks_per_beat
microseconds_per_beat = 60000000 // BPM
track.append(mido.MetaMessage('set_tempo', tempo=microseconds_per_beat, time=0))

# Criando as notas na trilha MIDI
time = 0
for n in notas:
    # Adicionando um silêncio
    if n is None:
        track.append(mido.Message('note_off', note=60, velocity=0, time=int(tick_per_beat * DURACAO_NOTAS)))
    # Adicionando uma nota
    else:
        track.append(mido.Message('note_on', note=n, velocity=VOLUME, time=int(tick_per_beat * DURACAO_NOTAS)))
    time += int(tick_per_beat * DURACAO_NOTAS)

# Salvando o arquivo MIDI
mid.save('musica3.mid')
