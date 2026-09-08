"""Calculadora gráfica com avaliação aritmética segura."""

from __future__ import annotations

import ast
import math
import operator
import tkinter as tk


_OPERADORES_BINARIOS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
}
_OPERADORES_UNARIOS = {
    ast.UAdd: operator.pos,
    ast.USub: operator.neg,
}


def avaliar_expressao(expressao: str) -> int | float:
    """Avalia somente números e os operadores exibidos pela calculadora."""
    if not expressao or len(expressao) > 100:
        raise ValueError("Expressão vazia ou longa demais")

    try:
        arvore = ast.parse(expressao, mode="eval")
    except SyntaxError as erro:
        raise ValueError("Expressão inválida") from erro

    def avaliar(no: ast.AST, profundidade: int = 0) -> int | float:
        if profundidade > 20:
            raise ValueError("Expressão complexa demais")

        if isinstance(no, ast.Expression):
            return avaliar(no.body, profundidade + 1)

        if isinstance(no, ast.Constant):
            if isinstance(no.value, bool) or not isinstance(no.value, (int, float)):
                raise ValueError("Somente números são permitidos")
            return no.value

        if isinstance(no, ast.BinOp) and type(no.op) in _OPERADORES_BINARIOS:
            esquerda = avaliar(no.left, profundidade + 1)
            direita = avaliar(no.right, profundidade + 1)
            resultado = _OPERADORES_BINARIOS[type(no.op)](esquerda, direita)
        elif isinstance(no, ast.UnaryOp) and type(no.op) in _OPERADORES_UNARIOS:
            resultado = _OPERADORES_UNARIOS[type(no.op)](
                avaliar(no.operand, profundidade + 1)
            )
        else:
            raise ValueError("Operação não permitida")

        if isinstance(resultado, float) and not math.isfinite(resultado):
            raise ValueError("Resultado fora do intervalo permitido")
        return resultado

    return avaliar(arvore)


class Calculadora(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Calculadora")
        self.geometry("300x400")
        self.resultado_var = tk.StringVar()
        self.criar_widgets()

    def criar_widgets(self) -> None:
        entrada = tk.Entry(
            self,
            textvariable=self.resultado_var,
            font=("Arial", 24),
            bd=10,
            relief=tk.GROOVE,
            justify=tk.RIGHT,
        )
        entrada.grid(row=0, column=0, columnspan=4)

        botoes = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+",
            "C",
        ]

        linha = 1
        coluna = 0
        for rotulo in botoes:
            tk.Button(
                self,
                text=rotulo,
                padx=20,
                pady=20,
                font=("Arial", 18),
                bd=8,
                relief=tk.RIDGE,
                command=lambda valor=rotulo: self.botao_click(valor),
            ).grid(row=linha, column=coluna)
            coluna += 1
            if coluna > 3:
                coluna = 0
                linha += 1

    def botao_click(self, valor: str) -> None:
        if valor == "=":
            try:
                self.resultado_var.set(avaliar_expressao(self.resultado_var.get()))
            except (ArithmeticError, TypeError, ValueError):
                self.resultado_var.set("Erro")
        elif valor == "C":
            self.resultado_var.set("")
        else:
            self.resultado_var.set(self.resultado_var.get() + valor)


if __name__ == "__main__":
    app = Calculadora()
    app.mainloop()
