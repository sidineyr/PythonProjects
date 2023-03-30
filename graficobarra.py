import matplotlib.pyplot as plt

# definindo os valores das barras
valores = [10, 20, 30, 100]

# definindo as posições das barras no eixo x
posicoes = [0, 1, 2, 3]

# criando o gráfico de barras
plt.bar(posicoes, valores)

# adicionando os rótulos do eixo x e y
plt.xlabel('Valores')
plt.ylabel('Contagem')

# adicionando o título do gráfico
plt.title('Gráfico de Barras')

# exibindo o gráfico
plt.show()

