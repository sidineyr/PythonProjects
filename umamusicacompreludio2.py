from midiutil.MidiFile import MIDIFile

# Criando o arquivo MIDI
midi = MIDIFile(1)
track = 0
time = 0
midi.addTrackName(track, time, "Minha Música")
midi.addTempo(track, time, 120)

# Adicionando o prelúdio
midi.addNote(track, 0, 60, 4, 0, 127)  # nota Dó
midi.addNote(track, 0, 64, 4, 0.5, 127)  # nota Mi

# Adicionando o primeiro interlúdio
midi.addNote(track, 0, 67, 4, 1, 127)  # nota Sol
midi.addNote(track, 0, 69, 4, 1.25, 127)  # nota Lá
midi.addNote(track, 0, 72, 4, 1.5, 127)  # nota Dó
midi.addNote(track, 0, 76, 4, 1.75, 127)  # nota Mi

# Adicionando o segundo interlúdio
midi.addNote(track, 0, 67, 4, 2, 127)  # nota Sol
midi.addNote(track, 0, 69, 4, 2.25, 127)  # nota Lá
midi.addNote(track, 0, 72, 4, 2.5, 127)  # nota Dó

# Salvando o arquivo MIDI
with open("minha_musica.mid", "wb") as output_file:
    midi.writeFile(output_file)
