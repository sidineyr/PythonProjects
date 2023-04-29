import random

# gerar um número aleatórrio de 0 a 10
numero_aleatorio = random.randint(0, 10)

# solicitar ao usuário que adivinhe o número
while True:
    palpite = int(input("Tente adivinhar o número de 0 a 10: "))

    # comparar o palpite com o número aleatório e fornecer uma resposta
    if palpite == numero_aleatorio:
        print("Parabéns, você acertou!")
        break
    else:
        if palpite > numero_aleatorio:
            print("O número é menor do que", palpite)
        else:
            print("O número é maior do que", palpite)
