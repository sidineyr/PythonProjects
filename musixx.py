from midiutil import MIDIFile
import random

# Configurações do arquivo MIDI
num_tracks = 1  # Número de pistas
tempo_bpm = 120  # BPM (batidas por minuto)
duration_sec = 60  # Duração em segundos

# Configurações das notas musicais
min_note = 48  # Nota mínima (C4)
max_note = 92  # Nota máxima (C7)
min_velocity = 60  # Velocidade mínima (0-127)
max_velocity = 100  # Velocidade máxima (0-127)

# Configurações do loop
loop_duration_sec = 10  # Duração de cada loop em segundos

# Cria um arquivo MIDI com o número de pistas especificado
midi_file = MIDIFile(num_tracks)

# Configura o tempo (BPM) do arquivo MIDI
midi_file.addTempo(0, 0, tempo_bpm)

# Calcula o número de notas musicais por segundo
notes_per_sec = len(range(min_note, max_note + 1)) / duration_sec


# Calcula o número de notas por loop
notes_per_loop = int(notes_per_sec * loop_duration_sec)

# Calcula o número total de loops
num_loops = int(duration_sec / loop_duration_sec)

# Cria um arquivo MIDI com o número de pistas especificado
midi_file = MIDIFile(num_tracks)

# Configura o tempo (BPM) do arquivo MIDI
midi_file.addTempo(0, 0, tempo_bpm)

# Gera as notas musicais aleatoriamente em loops de 8 segundos
for i in range(num_loops):
    # Calcula o tempo inicial do loop atual
    loop_start_time = i * loop_duration_sec

    # Gera as notas musicais aleatoriamente para o loop atual
    for j in range(notes_per_loop):
        # Calcula o tempo dentro do loop atual
        time_within_loop = j / notes_per_sec

        # Calcula o tempo para a nota atual
        time = loop_start_time + time_within_loop

        # Escolhe uma nota, uma velocidade e um tempo para a nota atual
        note = random.randint(min_note, max_note)
        velocity = random.randint(min_velocity, max_velocity)

        # Adiciona a nota à pista do arquivo MIDI
        midi_file.addNote(0, 0, note, time, 1, velocity)

# Salva o arquivo MIDI
with open("script_musical.mid", "wb") as output_file:
    midi_file.writeFile(output_file)
