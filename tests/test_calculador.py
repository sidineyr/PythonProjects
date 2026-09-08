import pytest

from calculador import avaliar_expressao


def test_avalia_operacoes_e_precedencia():
    assert avaliar_expressao("2+3*4") == 14
    assert avaliar_expressao("(10-2)/4") == 2
    assert avaliar_expressao("-3+1.5") == -1.5


@pytest.mark.parametrize(
    "expressao",
    [
        "__import__('os').system('echo inseguro')",
        "2**8",
        "[1, 2, 3]",
        "True",
    ],
)
def test_rejeita_codigo_e_operacoes_nao_exibidas(expressao):
    with pytest.raises(ValueError):
        avaliar_expressao(expressao)


def test_rejeita_divisao_por_zero():
    with pytest.raises(ZeroDivisionError):
        avaliar_expressao("1/0")
