from midiutil import MIDIFile
import pygame
import time
import random

# Definindo as notas e suas respectivas frequências MIDI
MIDI_NOTES = {'F': 65, 'G': 67, 'A': 69, 'B': 71, 'C': 72, 'D': 74, 'E': 76}

# Criando um objeto MIDIFile com 1 track
midi_file = MIDIFile(1)

# Definindo as configurações do arquivo MIDI
track = 0
channel = 0
time = 0  # Início no tempo 0
duration = 0.60  # Duração de cada nota (120ms)
volume = 87  # Volume máximo
tempo = 60  # 80 bpm
silence_duration = 0.18  # Duração de cada silêncio (20ms)

# Adicionando um tempo inicial ao arquivo MIDI
midi_file.addTempo(track, time, tempo)

# Gerando a sequência de notas aleatória sem repetir padrão de distribuição
notes_sequence = []
while len(notes_sequence) < 55:
    notes = random.sample(list(MIDI_NOTES.keys()), k=4)
    for note in notes:
        if len(notes_sequence) < 55:
            notes_sequence.append(note)

# Adicionando as notas e os silêncios ao arquivo MIDI
for i, note in enumerate(notes_sequence):
    if note == 'F':
        pitch = MIDI_NOTES['F']
    elif note == 'G':
        pitch = MIDI_NOTES['G']
    elif note == 'A':
        pitch = MIDI_NOTES['A']
    elif note == 'B':
        pitch = MIDI_NOTES['B']
    elif note == 'C':
        pitch = MIDI_NOTES['C']
    elif note == 'D':
        pitch = MIDI_NOTES['D']
    elif note == 'E':
        pitch = MIDI_NOTES['E']
        
    # Adicionando a nota ao arquivo MIDI
    midi_file.addNote(track, channel, pitch, time, duration, volume)
    
    # Adicionando o silêncio ao arquivo MIDI
    midi_file.addNote(track, channel, 0, time+duration, silence_duration, 0)
    
    # Atualizando o tempo para a próxima nota/silêncio
    time += duration + silence_duration

# Salvando o arquivo MIDI
with open("music.mid", "wb") as output_file:
    midi_file.writeFile(output_file)

# Tocando a música
pygame.mixer.init()
pygame.mixer.music.load("music.mid")
pygame.mixer.music.play()

# Esperando a música terminar
time.sleep(15)

# Parando a música e fechando o Pygame
pygame.mixer.music.stop()
pygame.quit()
