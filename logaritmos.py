from math import log10

# Define a base para os logaritmos
base = int(input("Digite a base dos logaritmos: "))

# Define o intervalo de valores para os quais os logaritmos serão calculados
start = int(input("Digite o valor inicial: "))
end = int(input("Digite o valor final: "))

# Cria um cabeçalho para a tabela
print("Tábua de Logaritmos (base %d)" % base)
print("Valor\tLogaritmo")

# Calcula e exibe os logaritmos para cada valor no intervalo especificado
for i in range(start, end + 1):
    if i > 0:
        log = log10(i) / log10(base)
        print("%d\t%0.5f" % (i, log))
    else:
        print("%d\tIndefinido" % i)
