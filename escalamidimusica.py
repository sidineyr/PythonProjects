from mingus.core import notes, chords, scales, midi
from mingus.containers import Bar
from mingus.midi import fluidsynth

# Configurações da escala, tempo e número de notas
scale = scales.get_scale('C', 'major')
num_notes = 280
num_silences = 280
tempo = 90

# Cria uma nova barra com a escala e o tempo especificados
bar = Bar(key='C', time_signature=(3, 4), tempo=tempo)

# Adiciona notas aleatórias na barra
for i in range(num_notes):
    note = notes.int_to_note(scale[int(len(scale) * i / num_notes)])
    bar.place_notes(note, 4)

# Adiciona silêncios na barra
for i in range(num_silences):
    bar.place_rest(4)

# Salva a barra em um arquivo MIDI
midi_file = 'random_scale.mid'
midi.save_composition(midi_file, [bar])

# Toca o arquivo MIDI utilizando o fluidsynth
fluidsynth.init('/usr/share/sounds/sf2/FluidR3_GM.sf2', 'alsa')
fluidsynth.play_MIDI(midi_file)
