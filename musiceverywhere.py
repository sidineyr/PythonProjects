import random
from midiutil import MIDIFile

# Configurações para o arquivo MIDI
scale = "G"  # Escala em Sol
bpm = 120  # BPM (batidas por minuto)
duration_1 = 30  # Duração em segundos da primeira parte
duration_2 = 30  # Duração em segundos da segunda parte
duration_3 = 10  # Duração em segundos da terceira parte
notes_1 = 20  # Número de notas na primeira parte
notes_2 = 40  # Número de notas na segunda parte
notes_3 = 10  # Número de notas na terceira parte
note_duration_1 = 0.08  # Duração de cada nota na primeira parte (80ms)
note_duration_2 = 0.1  # Duração de cada nota na segunda parte (100ms)
note_duration_3 = 0.16  # Duração de cada nota na terceira parte (160ms)
note_pause_1 = 0.03  # Intervalo entre as notas na primeira parte (30ms)
note_pause_2 = 0.02  # Intervalo entre as notas na segunda parte (20ms)
note_pause_3 = 0.02  # Intervalo entre as notas na terceira parte (20ms)

# Função para gerar notas aleatórias
def generate_random_notes(notes, duration, pause):
    note_list = []
    for i in range(notes):
        note = random.randint(60, 84)  # Notas de Sol (60) a Dó# (84)
        start_time = i * (duration + pause)
        note_list.append((note, start_time, duration))
    return note_list

# Gerar notas aleatórias para cada parte da música
notes_part_1 = generate_random_notes(notes_1, note_duration_1, note_pause_1)
notes_part_2 = generate_random_notes(notes_2, note_duration_2, note_pause_2)
notes_part_3 = generate_random_notes(notes_3, note_duration_3, note_pause_3)

# Criar um novo arquivo MIDI
midi_file = MIDIFile(1)  # 1 trilha
midi_file.addTempo(0, 0, bpm)  # Definir o BPM

# Adicionar as notas geradas ao arquivo MIDI
for note, start_time, duration in notes_part_1:
    midi_file.addNote(0, 0, note, start_time, duration, volume=127)

for note, start_time, duration in notes_part_2:
    midi_file.addNote(0, 0, note, start_time + duration_1, duration, volume=127)

for note, start_time, duration in notes_part_3:
    midi_file.addNote(0, 0, note, start_time + duration_1 + duration_2, duration, volume=127)

# Salvar o arquivo MIDI gerado
with open('maestropythondanose.mid', 'wb') as file:
    midi_file.writeFile(file)

# Tocar o arquivo MIDI usando o FluidSynth (ou outra biblioteca de sua escolha)
# Código para reprodução de arquivo MIDI não incluído aqui

