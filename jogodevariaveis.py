from pydub import AudioSegment
from pydub.generators import sine
from midiutil import MIDIFile

# Define a duração das notas e dos intervalos de silêncio em milissegundos
note_duration = 120
silence_duration = 80

# Define o número de notas em um compasso 4/4
notes_per_measure = 4

# Define o volume máximo para todas as notas
max_volume = 0.5

# Define a lista de notas musicais
notes = ["C", "D", "E", "F", "G", "A", "B"]

# Inicializa a lista de áudios e o tempo atual
audio_segments = []
current_time = 0

# Loop pelas notas musicais
for note in notes:
    # Gera uma onda sonora da nota
    frequency = AudioSegment.from_file(f"{note}.mp3").frame_rate
    audio = sine(frequency).to_audio_segment(duration=note_duration)

    # Define o volume da nota
    audio = audio - audio.dBFS + max_volume

    # Adiciona a nota à lista de áudios e atualiza o tempo atual
    audio_segments.append(audio)
    current_time += note_duration

    # Adiciona um intervalo de silêncio à lista de áudios e atualiza o tempo atual
    audio_segments.append(AudioSegment.silent(duration=silence_duration))
    current_time += silence_duration

    # Verifica se o compasso foi concluído e adiciona um intervalo de silêncio extra se necessário
    if len(audio_segments) % notes_per_measure == 0:
        audio_segments.append(AudioSegment.silent(duration=silence_duration))
        current_time += silence_duration

# Concatena todos os áudios em um único áudio
music = AudioSegment.empty()
for audio in audio_segments:
    music += audio

# Toca a música e a salva em um arquivo MIDI
music.export("testemusical.wav", format="wav")
midi_file = MIDIFile(1)
midi_file.addTrackName(0, 0, "Teste Musical")
midi_file.addTempo(0, 0, 120)
for i, note in enumerate(notes):
    midi_file.addNote(0, 0, i, current_time // 1000, note_duration / 1000, 100)
with open("testemusical.mid", "wb") as output_file:
    midi_file.writeFile(output_file)
