def imprimir_padrao(n):
    for i in range(1, n + 1):
        linha = '*' * i
    print(linha)

    for i in range(n - 1, 0, -1):
        linha = '*' * i
    print(linha)

if __name__ == "__main__":
    imprimir_padrao(5)
