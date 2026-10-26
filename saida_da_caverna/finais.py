"""Gera três conclusões para a miniatura "Saída da Caverna".

Os compassos 1–6 são copiados sem alterações da obra original. Somente os
compassos 7–8 mudam, permitindo comparar finais luminoso, suspenso e sereno.
"""

from copy import deepcopy
from pathlib import Path

from music21 import chord, note, stream

try:
    from .saida_da_caverna import criar_partitura
except ImportError:
    from saida_da_caverna import criar_partitura


OUTPUT_DIR = Path(__file__).resolve().parent
INICIO_DOS_FINAIS = 24.0

FINAIS = {
    "luminoso": {
        "acordes": ((["F2", "C3"], 48), (["G2", "D3"], 51), (["C3", "E3", "G3"], 55)),
        "melodia": ("F4", "G4", "C5"),
        "velocidades": (68, 74, 82),
    },
    "suspenso": {
        "acordes": ((["F2", "C3"], 48), (["G2", "D3"], 51), (["A2", "C3", "E3"], 52)),
        "melodia": ("F4", "G4", "A4"),
        "velocidades": (68, 72, 70),
    },
    "sereno": {
        "acordes": ((["D3", "F3"], 45), (["G2", "D3"], 48), (["C3", "E3", "G3"], 50)),
        "melodia": ("F4", "G4", "E5"),
        "velocidades": (62, 67, 72),
    },
}


def _remover_final(parte: stream.Part) -> None:
    for elemento in list(parte.notesAndRests):
        if float(elemento.offset) >= INICIO_DOS_FINAIS:
            parte.remove(elemento)


def criar_final(nome: str) -> stream.Score:
    if nome not in FINAIS:
        raise ValueError(f"Final desconhecido: {nome}. Use: {', '.join(FINAIS)}.")

    partitura = deepcopy(criar_partitura())
    partitura.id = f"SaidaDaCaverna_{nome.title()}"
    partitura.metadata.title = f"Saída da Caverna — final {nome}"
    melodia = partitura.getElementById("Melodia")
    harmonia = partitura.getElementById("Harmonia")
    _remover_final(melodia)
    _remover_final(harmonia)

    dados = FINAIS[nome]
    for altura, duracao, velocidade in zip(
        dados["melodia"], (2.0, 2.0, 3.75), dados["velocidades"], strict=True
    ):
        evento = note.Note(altura, quarterLength=duracao)
        evento.volume.velocity = velocidade
        melodia.append(evento)
    melodia.append(note.Rest(quarterLength=0.25))

    for (alturas, velocidade), duracao in zip(
        dados["acordes"], (2.0, 2.0, 4.0), strict=True
    ):
        evento = chord.Chord(alturas, quarterLength=duracao)
        evento.volume.velocity = velocidade
        harmonia.append(evento)
    return partitura


def gerar_midis() -> list[Path]:
    caminhos = []
    for nome in FINAIS:
        caminho = OUTPUT_DIR / f"final_{nome}.mid"
        criar_final(nome).write("midi", fp=caminho)
        caminhos.append(caminho)
        print(f"MIDI criado: {caminho}")
    return caminhos


if __name__ == "__main__":
    gerar_midis()
