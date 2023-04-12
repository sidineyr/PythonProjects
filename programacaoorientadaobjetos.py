# Exemplo de script Python que explica programação orientada a objetos

# Criando uma classe
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print("Oi, meu nome é " + self.nome + " e eu tenho " + str(self.idade) + " anos.")

# Criando um objeto da classe Pessoa
pessoa1 = Pessoa("João", 30)

# Chamando o método apresentar do objeto pessoa1
pessoa1.apresentar()

# Saída esperada: Oi, meu nome é João e eu tenho 30 anos.

# Explicação do código:

# O que é uma classe?
# Uma classe é um modelo ou plano que define as variáveis e funções que um objeto deve ter. É uma forma de criar um novo tipo de dado.

# No exemplo acima, criamos uma classe chamada Pessoa. Ela tem dois atributos: nome e idade. Ela também tem um método chamado apresentar, que imprime uma mensagem na tela.

# O que é um objeto?
# Um objeto é uma instância de uma classe. Quando criamos um objeto, estamos criando uma cópia da classe com os seus atributos e métodos.

# No exemplo acima, criamos um objeto da classe Pessoa chamado pessoa1. Definimos o nome como "João" e a idade como 30. Em seguida, chamamos o método apresentar do objeto pessoa1.

# O que é um método?
# Um método é uma função que pertence a uma classe. Quando chamamos um método de um objeto, estamos chamando uma função que está definida na classe.

# No exemplo acima, o método apresentar da classe Pessoa imprime uma mensagem na tela com o nome e a idade da pessoa.

# Conclusão:
# Programação orientada a objetos é uma forma de programar baseada em objetos. Um objeto é uma instância de uma classe, que é um modelo ou plano que define as variáveis e funções que o objeto deve ter. Usando classes e objetos, podemos organizar nosso código de forma mais modular e reutilizável, o que pode tornar nossos programas mais eficientes e fáceis de manter.
