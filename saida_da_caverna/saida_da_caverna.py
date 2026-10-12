"""Gera a miniatura para piano "Saída da Caverna" em MIDI.

Forma: apresentação (compassos 1–4), transformação (5–6) e chegada
(7–8). A escrita usa somente duas vozes e permanece em Dó maior.
"""

from pathlib import Path

from music21 import chord, instrument, key, meter, metadata, note, stream, tempo


OUTPUT_DIR = Path(__file__).resolve().parent
MIDI_PATH = OUTPUT_DIR / "saida_da_caverna.mid"


def nota(nome: str, duracao: float, velocidade: int) -> note.Note:
    """Cria uma nota de piano com duração e intensidade definidas."""
    n = note.Note(nome, quarterLength=duracao)
    n.volume.velocity = velocidade
    return n


def pausa(duracao: float) -> note.Rest:
    return note.Rest(quarterLength=duracao)


def acorde(nomes: list[str], duracao: float, velocidade: int) -> chord.Chord:
    c = chord.Chord(nomes, quarterLength=duracao)
    c.volume.velocity = velocidade
    return c


def criar_partitura() -> stream.Score:
    score = stream.Score(id="SaidaDaCaverna")
    score.metadata = metadata.Metadata()
    score.metadata.title = "Saída da Caverna"
    score.metadata.composer = "Sidiney Rodrigues"

    melodia = stream.Part(id="Melodia")
    melodia.partName = "Piano — melodia"
    melodia.insert(0, instrument.Piano())
    melodia.insert(0, meter.TimeSignature("4/4"))
    melodia.insert(0, key.Key("C"))
    melodia.insert(0, tempo.MetronomeMark(number=92))

    # Cada grupo contém dois compassos. Pequenas respirações de 0,2 semínima
    # evitam que a execução soe inteiramente mecânica.
    frases = [
        # Apresentação: um motivo hesitante de quatro notas.
        [("C4", 1.8, 54), (None, 0.2, 0), ("D4", 1.9, 61), (None, 0.1, 0),
         ("B3", 1.75, 50), (None, 0.25, 0), ("E4", 1.9, 64), (None, 0.1, 0)],
        # Repetição: apenas a última nota muda, abrindo o caminho para Sol.
        [("C4", 1.8, 57), (None, 0.2, 0), ("D4", 1.9, 63), (None, 0.1, 0),
         ("B3", 1.75, 53), (None, 0.25, 0), ("G4", 1.9, 70), (None, 0.1, 0)],
        # Transformação: o motivo sobe uma terça diatônica.
        [("E4", 1.8, 64), (None, 0.2, 0), ("F4", 1.9, 69), (None, 0.1, 0),
         ("D4", 1.75, 61), (None, 0.25, 0), ("G4", 1.9, 75), (None, 0.1, 0)],
        # Chegada: F–G–C, com a tônica sustentada até o fim.
        [("F4", 2.0, 68), ("G4", 2.0, 74), ("C5", 3.75, 82), (None, 0.25, 0)],
    ]
    for frase in frases:
        for altura, duracao, velocidade in frase:
            melodia.append(pausa(duracao) if altura is None else nota(altura, duracao, velocidade))

    harmonia = stream.Part(id="Harmonia")
    harmonia.partName = "Piano — harmonia"
    harmonia.insert(0, instrument.Piano())
    # Uma sustentação discreta por compasso deixa o motivo em primeiro plano.
    progressao = [
        (["C3", "G3"], 38), (["A2", "E3"], 36),
        (["C3", "G3"], 40), (["G2", "D3"], 42),
        (["C3", "G3"], 43), (["G2", "D3"], 45),
        (["F2", "C3"], 48), (["G2", "D3"], 51),
        (["C3", "E3", "G3"], 55),
    ]
    # O compasso 7 recebe F e G por dois tempos; os demais acordes duram 4.
    duracoes = [4, 4, 4, 4, 4, 4, 2, 2, 4]
    for (nomes, velocidade), duracao in zip(progressao, duracoes, strict=True):
        harmonia.append(acorde(nomes, duracao, velocidade))

    score.insert(0, melodia)
    score.insert(0, harmonia)
    return score


def main() -> None:
    partitura = criar_partitura()
    partitura.write("midi", fp=MIDI_PATH)
    print(f"MIDI criado: {MIDI_PATH}")


if __name__ == "__main__":
    main()
