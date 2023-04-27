import math

# função para calcular as raízes
def calcular_raizes(a, b, c):
    delta = b ** 2 - 4 * a * c

    if delta < 0:
        return "Não há raízes reais"

    elif delta == 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        return f"Raiz única: x = {x1}"

    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return f"Duas raízes: x1 = {x1}, x2 = {x2}"

# pede ao usuário os valores de a, b e c
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

# calcula as raízes e exibe o resultado
resultado = calcular_raizes(a, b, c)
print(resultado)
