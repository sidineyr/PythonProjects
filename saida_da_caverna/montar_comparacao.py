"""Monta um WAV com os três finais separados por dois segundos de silêncio."""

from pathlib import Path
import wave


PASTA = Path(__file__).resolve().parent
ENTRADAS = [PASTA / f"final_{nome}.wav" for nome in ("luminoso", "suspenso", "sereno")]
SAIDA = PASTA / "comparacao_tres_finais.wav"


def montar_comparacao() -> Path:
    parametros = None
    trechos = []
    for caminho in ENTRADAS:
        with wave.open(str(caminho), "rb") as arquivo:
            atuais = arquivo.getparams()
            assinatura = (atuais.nchannels, atuais.sampwidth, atuais.framerate, atuais.comptype)
            if parametros is None:
                parametros = assinatura
            elif assinatura != parametros:
                raise ValueError(f"Formato incompatível em {caminho.name}")
            trechos.append(arquivo.readframes(atuais.nframes))

    canais, largura, taxa, _ = parametros
    silencio = b"\0" * (taxa * 2 * canais * largura)
    with wave.open(str(SAIDA), "wb") as arquivo:
        arquivo.setnchannels(canais)
        arquivo.setsampwidth(largura)
        arquivo.setframerate(taxa)
        for indice, trecho in enumerate(trechos):
            if indice:
                arquivo.writeframes(silencio)
            arquivo.writeframes(trecho)
    print(f"Comparação criada: {SAIDA}")
    return SAIDA


if __name__ == "__main__":
    montar_comparacao()
