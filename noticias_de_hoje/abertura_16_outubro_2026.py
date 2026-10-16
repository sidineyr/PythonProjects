"""Abertura musical de notícias — 16 de outubro de 2026.

Requer: pip install music21
Gera: abertura_noticias_2026-10-16.mid
"""

from music21 import chord, instrument, key, meter, metadata, note, stream, tempo


OUTFILE = "abertura_noticias_2026-10-16.mid"


def add_phrase(part, events, velocity=84):
    """Adiciona uma frase de pares (altura MIDI, duração em semínimas)."""
    for pitch, duration in events:
        event = note.Rest(quarterLength=duration) if pitch is None else note.Note(pitch)
        event.quarterLength = duration
        if pitch is not None:
            event.volume.velocity = velocity
        part.append(event)


score = stream.Score(id="AberturaDasNoticias")
score.metadata = metadata.Metadata()
score.metadata.title = "Abertura das Notícias"
score.metadata.composer = "Sidiney Rodrigues"
score.metadata.date = "2026-10-16"

for part in (score,):
    part.append(tempo.MetronomeMark(number=132))
    part.append(meter.TimeSignature("4/4"))
    part.append(key.Key("D"))

brass = stream.Part(id="Fanfarra")
brass.insert(0, instrument.Trumpet())
melody = stream.Part(id="Manchetes")
melody.insert(0, instrument.Flute())
harmony = stream.Part(id="Horizonte")
harmony.insert(0, instrument.StringInstrument())

# A fanfarra abre com impulso ascendente e reaparece como assinatura no final.
for pitches in ([50, 57, 62], [52, 59, 64], [54, 61, 66], [55, 62, 67]):
    hit = chord.Chord(pitches, quarterLength=1)
    hit.volume.velocity = 96
    brass.append(hit)
brass.append(note.Rest(quarterLength=2))
for pitches in ([57, 62, 66], [55, 62, 67]):
    hit = chord.Chord(pitches, quarterLength=1)
    hit.volume.velocity = 102
    brass.append(hit)

# Motivo cantável em Ré maior: notícia, pausa, horizonte, volta.
add_phrase(
    melody,
    [
        (74, 0.5), (78, 0.5), (81, 1), (78, 0.5), (74, 0.5), (76, 1),
        (78, 0.5), (81, 0.5), (83, 1), (81, 0.5), (78, 0.5), (74, 1),
        (76, 0.5), (78, 0.5), (81, 1), (83, 0.5), (81, 0.5), (78, 1),
        (74, 0.5), (76, 0.5), (78, 1), (74, 0.5), (69, 0.5), (74, 1),
    ],
    velocity=92,
)

for tones in ([50, 54, 57], [45, 49, 52], [43, 47, 50], [50, 54, 57],
              [47, 50, 54], [45, 49, 52], [43, 47, 50], [50, 54, 57]):
    pad = chord.Chord(tones, quarterLength=1)
    pad.volume.velocity = 58
    harmony.append(pad)

score.insert(0, brass)
score.insert(0, harmony)
score.insert(0, melody)
score.write("midi", fp=OUTFILE)
print(f"MIDI criado: {OUTFILE}")

# A versão MIDI acompanha esta composição no repositório.
