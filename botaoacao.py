import tkinter as tk

def calcular_soma():
    # obtém os valores dos campos de entrada
    produto1 = float(entrada_produto1.get())
    produto2 = float(entrada_produto2.get())

    # calcula a soma dos produtos
    resultado = produto1 + produto2

    # atualiza o label com o resultado
    label_resultado.config(text="Resultado: %.2f" % resultado)

# cria a janela
janela = tk.Tk()
janela.title("Calculadora de Soma")

# cria os campos de entrada
tk.Label(janela, text="Produto 1:").grid(row=0, column=0)
entrada_produto1 = tk.Entry(janela)
entrada_produto1.grid(row=0, column=1)

tk.Label(janela, text="Produto 2:").grid(row=1, column=0)
entrada_produto2 = tk.Entry(janela)
entrada_produto2.grid(row=1, column=1)

# cria o botão de calcular
botao_calcular = tk.Button(janela, text="Calcular", command=calcular_soma)
botao_calcular.grid(row=2, column=0, columnspan=2)

# cria o label para exibir o resultado
label_resultado = tk.Label(janela, text="")
label_resultado.grid(row=3, column=0, columnspan=2)

# inicia a janela
janela.mainloop()
