from midiutil.MidiFile import MIDIFile
import random

# Definindo as configurações das notas musicais
first_30s_notes = 160
first_30s_note_duration = 180  # em milissegundos
first_30s_silence_duration = 90  # em milissegundos

next_30s_notes = 110
next_30s_note_duration = 100  # em milissegundos
next_30s_silence_duration = 20  # em milissegundos

final_10s_notes = 40
final_10s_note_duration = 130  # em milissegundos
final_10s_silence_duration = 10  # em milissegundos

# Função para gerar uma nota musical aleatória
def generate_random_note():
    note = random.randint(60, 71)  # Notas da escala de Sol (60 a 71)
    velocity = 127  # Volume máximo
    duration = 0  # Duração inicial
    return note, velocity, duration

# Criar um novo arquivo MIDI
midi_file = MIDIFile(1)
track = 0
time = 0

# Configurar o tempo do MIDI para 4/4
midi_file.addTimeSignature(track, time, 4, 2, 24, 8)

# Gerar as notas para os primeiros 30 segundos
for _ in range(first_30s_notes):
    note, velocity, duration = generate_random_note()
    midi_file.addNote(track, 0, note, time / 1000.0, first_30s_note_duration / 1000.0, velocity)
    time += first_30s_note_duration + first_30s_silence_duration

# Gerar as notas para os próximos 30 segundos
for _ in range(next_30s_notes):
    note, velocity, duration = generate_random_note()
    midi_file.addNote(track, 0, note, time / 1000.0, next_30s_note_duration / 1000.0, velocity)
    time += next_30s_note_duration + next_30s_silence_duration

# Gerar as notas para os últimos 10 segundos
for _ in range(final_10s_notes):
    note, velocity, duration = generate_random_note()
    midi_file.addNote(track, 0, note, time / 1000.0, final_10s_note_duration / 1000.0, velocity)
    time += final_10s_note_duration + final_10s_silence_duration

# Salvar o arquivo MIDI
with open("maestropython.mid", "wb") as output_file:
    midi_file.writeFile(output_file)
