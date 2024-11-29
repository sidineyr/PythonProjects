from music21 import stream, tempo, meter, chord, note, instrument, midi

# 1. Configuração inicial
# Cria um fluxo principal para a música
composition = stream.Score()

# Define o tempo (90 BPM) e a assinatura de tempo (4/4)
composition.append(tempo.MetronomeMark(number=90))
composition.append(meter.TimeSignature('4/4'))

# Função auxiliar para criar acordes de uma progressão
def create_chord_progression(progression, duration=4):
    return [chord.Chord(p, quarterLength=duration) for p in progression]

# 2. Prelúdio: Piano tocando acordes com arpejos
piano = stream.Part()
piano.insert(0, instrument.Piano())

# Adiciona os acordes em compassos
prelude_progression = [['C4', 'E4', 'G4'], ['G3', 'B3', 'D4'], ['A3', 'C4', 'E4'], ['F3', 'A3', 'C4']]
for _ in range(2):  # 8 compassos no total
    for chord_notes in prelude_progression:
        measure = stream.Measure()
        measure.append(chord.Chord(chord_notes, quarterLength=4))
        piano.append(measure)

# 3. Interlúdio: Violino e bateria
violin = stream.Part()
violin.insert(0, instrument.Violin())

melody_notes = ['E5', 'F5', 'G5', 'A5', 'B5', 'C6', 'B5', 'A5']  # Melodia simples
for n in melody_notes * 2:  # Repetir para 16 compassos
    measure = stream.Measure()
    measure.append(note.Note(n, quarterLength=1))
    violin.append(measure)

# Bateria com ritmo sutil
drums = stream.Part()
drums.insert(0, instrument.Woodblock())
for _ in range(16):  # 16 compassos
    measure = stream.Measure()
    measure.append(note.Rest(quarterLength=1))
    measure.append(note.Note('C2', quarterLength=1))  # Batida simples
    measure.append(note.Rest(quarterLength=1))
    measure.append(note.Note('C2', quarterLength=1))
    drums.append(measure)

# 4. Finalização: Piano e violino juntos
final_progression = [['C4', 'E4', 'G4', 'B4']]  # Acorde suspenso final
for chord_notes in final_progression:
    measure = stream.Measure()
    measure.append(chord.Chord(chord_notes, quarterLength=4))
    piano.append(measure)
    violin.append(measure)

# 5. Adicionando as partes ao fluxo principal
composition.append(piano)
composition.append(violin)
composition.append(drums)

# 6. Exportando para MIDI
midi_file = midi.translate.music21ObjectToMidiFile(composition)
midi_file.open('composition_fixed.mid', 'wb')
midi_file.write()
midi_file.close()

print("Composição gerada e salva como 'composition_fixed.mid'.")
