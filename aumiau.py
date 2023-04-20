from midiutil import MIDIFile

# Duração de cada som em segundos
duracao_miau_gato = 0.5
duracao_latido_cachorro = 0.25

# Crie um novo arquivo MIDI com uma pista de áudio
midi_file = MIDIFile(1)  # 1 pista de áudio
midi_file.addTrackName(0, 0, "Conversa de Gato e Cachorro")  # Nome da pista
midi_file.addTempo(0, 0, 120)  # BPM da música

# Notas musicais representando a conversa (usando notas fictícias)
# Gato mia duas vezes
for i in range(2):
    nota_miau = 60  # Nota C4
    inicio = i * duracao_miau_gato
    midi_file.addNote(0, 0, nota_miau, inicio, duracao_miau_gato, volume=100) 

# Cachorro late quatro vezes
for i in range(4):
    nota_latido = 62  # Nota D4
    inicio = (2 * duracao_miau_gato) + (i * duracao_latido_cachorro)
    midi_file.addNote(0, 0, nota_latido, inicio, duracao_latido_cachorro, volume=100)

# Gato responde uma vez
nota_miau_resposta = 63  # Nota D#4
inicio = (2 * duracao_miau_gato) + (4 * duracao_latido_cachorro)
midi_file.addNote(0, 0, nota_miau_resposta, inicio, duracao_miau_gato, volume=100)

# Cachorro late três vezes
for i in range(3):
    nota_latido = 62  # Nota D4
    inicio = (2 * duracao_miau_gato) + (5 * duracao_latido_cachorro) + (i * duracao_latido_cachorro)
    midi_file.addNote(0, 0, nota_latido, inicio, duracao_latido_cachorro, volume=100)

# Salve o arquivo MIDI em disco
with open("conversa.mid", "wb") as output_file:
    midi_file.writeFile(output_file)
