import random
from midiutil import MIDIFile

X = {
    0: "C",
    1: "D",
    2: "E",
    3: "F",
    4: "G",
    5: "A",
    6: "B",
}

# Gerar a sequência de notas aleatórias
notas_aleatorias = random.sample(list(X.values()), len(X))

# Configurações para o arquivo MIDI
midi = MIDIFile(1)
track = 0
midi.addTrackName(track, 0, "Música gerada")
midi.addTempo(track, 0, 120)

# Adicionar notas à sequência MIDI
for nota in notas_aleatorias:
    midi.addNote(
        track,
        0,
        X.keys()[X.values().index(nota)],
        0.0,
        0.12, # duração de 120ms
        127, # volume máximo
    )
    midi.addNote(
        track,
        0,
        0, # pausa
        0.12,
        0.08, # duração do silêncio de 80ms
        0, # volume zero
    )

# Salvar arquivo MIDI
with open("musica.mid", "wb") as output_file:
    midi.writeFile(output_file)
