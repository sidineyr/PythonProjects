from midiutil import MIDIFile
import random

# Define as constantes para o arquivo MIDI
TEMPO = 120
DURACAO_NOTA = 0.9
VOLUME = 100

# Define a estrutura da música com os tempos de cada seção
PRELUDIO_TEMPO = 30
INTERLUDIO_TEMPO = 60
POSLUDIO_TEMPO = 30
TEMPO_TOTAL = PRELUDIO_TEMPO + INTERLUDIO_TEMPO + POSLUDIO_TEMPO

# Define o número total de notas na música
NUM_NOTAS = 240

# Cria um objeto MIDIFile com uma única track
midi_file = MIDIFile(1)

# Adiciona um track name e um tempo ao arquivo MIDI
track = 0
time = 0
midi_file.addTrackName(track, time, "Exemplo de música aleatória")
midi_file.addTempo(track, time, TEMPO)

# Cria uma sequência de notas e silêncios aleatórios
notas = [random.randint(60, 72) for i in range(NUM_NOTAS)]
silencios = [0 for i in range(NUM_NOTAS)]
seq = []
for i in range(NUM_NOTAS):
    seq.append(notas[i])
    seq.append(silencios[i])

# Define o tempo de início de cada seção da música
preludio_inicio = 0
interludio_inicio = PRELUDIO_TEMPO
posludio_inicio = PRELUDIO_TEMPO + INTERLUDIO_TEMPO

# Adiciona as notas e os silêncios à música com o tempo apropriado
for i, pitch in enumerate(seq):
    if i < NUM_NOTAS * (PRELUDIO_TEMPO / TEMPO_TOTAL):
        tempo = TEMPO * (i / 2) + preludio_inicio
    elif i < NUM_NOTAS * ((PRELUDIO_TEMPO + INTERLUDIO_TEMPO) / TEMPO_TOTAL):
        tempo = TEMPO * (i / 2) + interludio_inicio
    else:
        tempo = TEMPO * (i / 2) + posludio_inicio
    midi_file.addNote(track, 0, pitch, tempo, DURACAO_NOTA, VOLUME)

# Escreve o arquivo MIDI
with open("exemplo.mid", "wb") as output_file:
    midi_file.writeFile(output_file)
