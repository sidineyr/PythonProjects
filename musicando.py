from midiutil import MIDIFile
import pygame
import time

# Definindo as constantes
TEMPO = 80  # bpm
DURACAO_NOTA = 0.5  # em segundos
VOLUME = 127
NOTAS = [65, 67, 72]  # fá, sol e dó na oitava 4

# Criando o arquivo MIDI
midi_file = MIDIFile(1)
midi_file.addTempo(track=0, time=0, tempo=TEMPO)

# Adicionando as notas
for i in range(4):
    for nota in NOTAS:
        midi_file.addNote(track=0, channel=0, pitch=nota, time=i*DURACAO_NOTA*2, duration=DURACAO_NOTA, volume=VOLUME)

# Gravando o arquivo MIDI em um arquivo
with open("melodia.mid", "wb") as output_file:
    midi_file.writeFile(output_file)

# Inicializando o mixer Pygame
pygame.mixer.init()

# Carregando o arquivo MIDI e tocando a música
pygame.mixer.music.load("melodia.mid")
pygame.mixer.music.play()

# Aguardando o término da música
time.sleep(15)

# Parando a música e encerrando o mixer
pygame.mixer.music.stop()
pygame.mixer.quit()
