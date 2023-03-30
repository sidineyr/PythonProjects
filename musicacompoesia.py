from gtts import gTTS
import os

# Definindo a poesia
poesia = "Máquina de infinitas possibilidades,\nMestre dos algoritmos e dos números,\nComputador, meu amigo das verdades."

# Gerando o arquivo de áudio com a voz da língua portuguesa
tts = gTTS(poesia, lang='pt')
tts.save('poesia.mp3')

# Reproduzindo o arquivo de áudio
os.system('mpg321 poesia.mp3')


