from midiutil import MIDIFile
import time

# Definindo as notas musicais em MIDI
MIDI_NOTES = {
    'C': 60,
    'D': 62,
    'E': 64,
    'F': 65,
    'G': 67,
    'A': 69,
    'B': 71
}

# Definindo as notas da música
notes = ['F', 'E', 'C', 'A'] * 30

# Configurando os parâmetros da música
volume = 127
duration = 0.12 # 120ms
silence = 0.12 # 20ms
bpm = 60
time_per_beat = 40 / bpm
total_time = len(notes) * (duration + silence)

# Criando o arquivo MIDI
midi_file = MIDIFile(1)

# Configurando o tempo
midi_file.addTempo(0, 0, bpm)

# Adicionando as notas à trilha
for i, note in enumerate(notes):
    pitch = MIDI_NOTES[note]
    start_time = i * (duration + silence)
    midi_file.addNote(
        0, # trilha
        0, # canal
        pitch,
        start_time,
        duration,
        volume
    )

# Salvando o arquivo MIDI
with open('music.mid', 'wb') as output_file:
    midi_file.writeFile(output_file)

# Tocando a música
from pygame import mixer
mixer.init()
mixer.music.load('ricavalori.mid')
mixer.music.play()

# Esperando o fim da música
time.sleep(total_time)

# Encerrando o mixer
mixer.music.stop()
mixer.quit()
