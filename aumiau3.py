from midiutil import MIDIFile

# Duração de cada nota em segundos
duracao_miado_gato = 0.12
duracao_latido_cachorro = 0.08
duracao_silencio_gato = 0.03
duracao_silencio_cachorro = 0.02

# Notas musicais
notas_gato = [64, 71]  # Mi, Si
notas_cachorro = [60, 67, 69]  # Dó, Sol, Lá

# Padrão da conversa entre o gato e o cachorro
padrao_gato = [2, 2, 1, 4, 1]
padrao_cachorro = [3, 3, 5]

# Cria um novo arquivo MIDI com 1 faixa
midi_file = MIDIFile(1)

# Configuração das trilhas MIDI
trilha = 0
canal_gato = 0
canal_cachorro = 1
volume = 100

# Abre a trilha do gato
midi_file.addTrackName(trilha, 0, "Gato")
midi_file.addProgramChange(trilha, canal_gato, 0, 0)

# Abre a trilha do cachorro
midi_file.addTrackName(trilha, 1, "Cachorro")
midi_file.addProgramChange(trilha, canal_cachorro, 0, 26)

# Reproduz a conversa 5 vezes a partir do latido
for i in range(5):
    for nota_cachorro, repeticao_cachorro in zip(notas_cachorro, padrao_cachorro):
        for _ in range(repeticao_cachorro):
            inicio = i * (len(padrao_gato) * (duracao_miado_gato + duracao_silencio_gato) + len(padrao_cachorro) * (duracao_latido_cachorro + duracao_silencio_cachorro)) + padrao_cachorro.index(repeticao_cachorro) * (duracao_latido_cachorro + duracao_silencio_cachorro)
            midi_file.addNote(trilha, canal_cachorro, nota_cachorro, inicio, duracao_latido_cachorro, volume=volume)

    for nota_gato, repeticao_gato in zip(notas_gato, padrao_gato):
        for _ in range(repeticao_gato):
            inicio = i * (len(padrao_gato) * (duracao_miado_gato + duracao_silencio_gato) + len(padrao_cachorro) * (duracao_latido_cachorro + duracao_silencio_cachorro)) + padrao_gato.index(repeticao_gato) * (duracao_miado_gato + duracao_silencio_gato)
            midi_file.addNote(trilha, canal_gato, nota_gato, inicio, duracao_miado_gato, volume=volume)

# Salva o arquivo MIDI
with open("conversafinaldogato.mid", "wb") as arquivo:
    midi_file.writeFile(arquivo)
