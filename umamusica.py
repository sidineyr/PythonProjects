from midiutil import MIDIFile

# Cria um novo arquivo MIDI com uma única faixa
midi = MIDIFile(1)

# Define as configurações básicas do arquivo MIDI
track = 0
time = 0
midi.addTrackName(track, time, "Música Alegre")
midi.addTempo(track, time, 120)

# Define os parâmetros das notas
channel = 0
volume = 100
duration = 1

# Define as notas da música
notes = [60, 62, 64, 65, 67, 69, 71, 72]

# Adiciona as notas ao arquivo MIDI
for i, note in enumerate(notes):
    midi.addNote(track, channel, note, time + i * duration, duration, volume)

# Escreve o arquivo MIDI
with open("alegre.mid", "wb") as output_file:
    midi.writeFile(output_file)
