from saida_da_caverna.finais import FINAIS, criar_final
from saida_da_caverna.saida_da_caverna import criar_partitura


def _eventos_antes_do_final(parte):
    return [
        (e.offset, e.quarterLength, tuple(p.nameWithOctave for p in e.pitches))
        for e in parte.notes
        if float(e.offset) < 24.0
    ]


def test_tres_finais_preservam_os_seis_primeiros_compassos():
    referencia = [_eventos_antes_do_final(p) for p in criar_partitura().parts]
    assert set(FINAIS) == {"luminoso", "suspenso", "sereno"}
    for nome in FINAIS:
        versao = criar_final(nome)
        assert [_eventos_antes_do_final(p) for p in versao.parts] == referencia
        assert all(p.highestTime == 32 for p in versao.parts)


def test_harmonias_e_notas_finais():
    esperado = {
        "luminoso": (("F", "G", "C"), "C5"),
        "suspenso": (("F", "G", "A"), "A4"),
        "sereno": (("D", "G", "C"), "E5"),
    }
    for nome, (fundamentais, nota_final) in esperado.items():
        melodia, harmonia = criar_final(nome).parts
        acordes = [c for c in harmonia.recurse().getElementsByClass("Chord") if c.offset >= 24]
        assert tuple(c.root().name for c in acordes) == fundamentais
        assert melodia.recurse().notes[-1].nameWithOctave == nota_final
