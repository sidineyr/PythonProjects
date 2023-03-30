import matplotlib.pyplot as plt
import random

# definindo os valores e rótulos das fatias
valores = [random.randint(1, 10) for _ in range(5)]
rotulos = ['Fatia 1', 'Fatia 2', 'Fatia 3', 'Fatia 4', 'Fatia 5']

# criando o gráfico de pizza
plt.pie(valores, labels=rotulos)

# adicionando o título do gráfico
plt.title('Gráfico de Pizza')

# exibindo o gráfico
plt.show()
