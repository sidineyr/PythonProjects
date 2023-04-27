import tkinter as tk

def calcular_soma():
    # obtém os valores dos campos de entrada
    produto1 = float(entrada_produto1.get())
    produto2 = float(entrada_produto2.get())

    # calcula a soma dos produtos
    resultado = produto1 + produto2

    # atualiza o label com o resultado
    label_resultado.config(text="Resultado: %.2f" % resultado)

def calcular_subtracao():
    # obtém os valores dos campos de entrada
    produto1 = float(entrada_produto1.get())
    produto2 = float(entrada_produto2.get())

    # calcula a subtração dos produtos
    resultado = produto1 - produto2

    # atualiza o label com o resultado
    label_resultado.config(text="Resultado: %.2f" % resultado)

def calcular_multiplicacao():
    # obtém os valores dos campos de entrada
    produto1 = float(entrada_produto1.get())
    produto2 = float(entrada_produto2.get())

    # calcula a multiplicação dos produtos
    resultado = produto1 * produto2

    # atualiza o label com o resultado
    label_resultado.config(text="Resultado: %.2f" % resultado)

def calcular_divisao():
    # obtém os valores dos campos de entrada
    produto1 = float(entrada_produto1.get())
    produto2 = float(entrada_produto2.get())

    # verifica se o segundo produto é diferente de zero
    if produto2 == 0:
        label_resultado.config(text="Não é possível dividir por zero")
        return

    # calcula a divisão dos produtos
    resultado = produto1 / produto2

    # atualiza o label com o resultado
    label_resultado.config(text="Resultado: %.2f" % resultado)


# cria a janela
janela = tk.Tk()
janela.title("Calculadora de Soma, Subtração, Multiplicação e Divisão")

# cria os campos de entrada
tk.Label(janela, text="Produto 1:").grid(row=0, column=0)
entrada_produto1 = tk.Entry(janela)
entrada_produto1.grid(row=0, column=1)

tk.Label(janela, text="Produto 2:").grid(row=1, column=0)
entrada_produto2 = tk.Entry(janela)
entrada_produto2.grid(row=1, column=1)

# cria os botões de cálculo
botao_soma = tk.Button(janela, text="Somar", command=calcular_soma)
botao_soma.grid(row=2, column=0)

botao_subtracao = tk.Button(janela, text="Subtrair", command=calcular_subtracao)
botao_subtracao.grid(row=2, column=1)

botao_multiplicacao = tk.Button(janela, text="Multiplicar", command=calcular_multiplicacao)
botao_multiplicacao.grid(row=2, column=2)

botao_divisao = tk.Button(janela, text="Dividir", command=calcular_divisao)
botao_divisao.grid(row=2, column=3)

# cria o label para exibir o resultado
label_resultado = tk.Label(janela, text="")
label_resultado.grid(row=3, column=0, columnspan=4)

# inicia a janela
janela.mainloop()
