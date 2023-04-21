# Função para imprimir o tabuleiro
def imprimir_tabuleiro(tabuleiro):
    for i in range(3):
        for j in range(3):
            print(tabuleiro[i][j], end=" ")
        print()

# Função para verificar o vencedor
def verificar_vencedor(tabuleiro, jogador):
    # Verificar linhas
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] == jogador:
            return True

    # Verificar colunas
    for j in range(3):
        if tabuleiro[0][j] == tabuleiro[1][j] == tabuleiro[2][j] == jogador:
            return True

    # Verificar diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:
        return True

    return False

# Função para verificar empate
def verificar_empate(tabuleiro):
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == ' ':
                return False
    return True

# Função para realizar um movimento
def fazer_movimento(tabuleiro, jogador, linha, coluna):
    if tabuleiro[linha][coluna] == ' ':
        tabuleiro[linha][coluna] = jogador
        return True
    else:
        return False

# Função principal do jogo
def jogo_da_velha():
    tabuleiro = [[' ', ' ', ' '],
                 [' ', ' ', ' '],
                 [' ', ' ', ' ']]
    jogador = 'X'
    vencedor = False

    print("Bem-vindo(a) ao Jogo da Velha!")
    imprimir_tabuleiro(tabuleiro)

    while not vencedor and not verificar_empate(tabuleiro):
        linha = int(input("Jogador " + jogador + ", informe a linha (0-2): "))
        coluna = int(input("Jogador " + jogador + ", informe a coluna (0-2): "))

        if fazer_movimento(tabuleiro, jogador, linha, coluna):
            imprimir_tabuleiro(tabuleiro)
            if verificar_vencedor(tabuleiro, jogador):
                print("Jogador " + jogador + " venceu!")
                vencedor = True
            else:
                if jogador == 'X':
                    jogador = 'O'
                else:
                    jogador = 'X'
        else:
            print("Movimento inválido. Tente novamente.")

    if not vencedor:
        print("Empate!")

# Executar o jogo
jogo_da_velha()
