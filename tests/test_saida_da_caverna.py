from saida_da_caverna.saida_da_caverna import criar_partitura


def test_forma_e_material_melodico():
    score = criar_partitura()
    melodia, harmonia = score.parts

    alturas = [n.nameWithOctave for n in melodia.recurse().notes]
    assert alturas[:4] == ["C4", "D4", "B3", "E4"]
    assert alturas[4:8] == ["C4", "D4", "B3", "G4"]
    assert alturas[8:12] == ["E4", "F4", "D4", "G4"]
    assert alturas[12:] == ["F4", "G4", "C5"]

    assert len(score.parts) == 2
    assert melodia.highestTime == 32
    assert harmonia.highestTime == 32
