from midiutil import MIDIFile
import random

# Configurações do arquivo MIDI
num_tracks = 1  # Número de pistas
tempo_bpm = 120  # BPM (batidas por minuto)
duration_sec = 60  # Duração em segundos

# Configurações das notas musicais
notes = ['D', 'C', 'G', 'G', 'D', 'G', 'E', 'E', 'C', 'C', 'G', 'C', 'A', 'F', 'B', 'E', 'G', 'F', 'C', 'F', 'F', 'C', 'B', 'E', 'D', 'C', 'C', 'G', 'B', 'G', 'B', 'B', 'F', 'G', 'A', 'B', 'D', 'C', 'C', 'B', 'C', 'D', 'E', 'A', 'F', 'G', 'G', 'F', 'F', 'A']  # Lista de notas musicais
octaves = [4, 5, 6]  # Lista de oitavas
min_velocity = 60  # Velocidade mínima (0-127)
max_velocity = 100  # Velocidade máxima (0-127)

# Cria um arquivo MIDI com o número de pistas especificado
midi_file = MIDIFile(num_tracks)

# Configura o tempo (BPM) do arquivo MIDI
midi_file.addTempo(0, 0, tempo_bpm)

# Calcula o número de notas musicais por segundo
notes_per_sec = len(notes) * len(octaves) / duration_sec

# Gera as notas musicais aleatoriamente
for i in range(150):
    # Escolhe uma nota, uma oitava, uma velocidade e um tempo para a nota atual
    note = random.choice(notes)
    octave = random.choice(octaves)
    velocity = random.randint(min_velocity, max_velocity)
    time = i / notes_per_sec  # Tempo em segundos

    # Calcula o valor MIDI da nota atual
    note_midi = (octave + 1) * 12 + notes.index(note)

    # Adiciona a nota à pista do arquivo MIDI
    midi_file.addNote(0, 0, note_midi, time, 1, velocity)

# Salva o arquivo MIDI
with open("script_musical.mid", "wb") as output_file:
    midi_file.writeFile(output_file)


