import numpy as np
import pandas as pd
import random

# Define as dimensões da matriz aleatória
linhas = 100
colunas = 5

# Gera uma matriz aleatória de números e letras
matriz = np.empty((linhas, colunas), dtype='object')
for i in range(linhas):
    for j in range(colunas):
        if random.random() < 0.5:
            matriz[i, j] = random.randint(0, 100)
        else:
            matriz[i, j] = random.choice('abcdefghijklmnopqrstuvwxyz')

# Cria um DataFrame a partir da matriz
df = pd.DataFrame(matriz, columns=['Coluna 1', 'Coluna 2', 'Coluna 3', 'Coluna 4', 'Coluna 5'])

# Escreve o DataFrame em um arquivo CSV
df.to_csv('dados_aleatorios.csv', index=False)
