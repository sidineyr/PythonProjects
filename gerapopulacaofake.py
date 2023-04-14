from faker import Faker
import random
import csv

fake = Faker('pt_BR')  # Configura o gerador de dados para o português do Brasil

# Cria uma lista vazia para armazenar as pessoas
pessoas = []

# Loop para gerar 600 pessoas
for i in range(600):
    # Gera nome e sobrenome aleatórios
    nome = fake.first_name()
    sobrenome = fake.last_name()

    # Gera data de nascimento aleatória (entre 18 e 70 anos atrás)
    idade = random.randint(18, 70)
    data_nascimento = fake.date_of_birth(tzinfo=None, minimum_age=idade, maximum_age=idade)

    # Gera cidade de nascimento aleatória
    cidade = fake.city()

    # Adiciona as informações da pessoa à lista de pessoas
    pessoas.append([nome, sobrenome, data_nascimento, cidade])

# Escreve os dados em um arquivo CSV
with open('pessoas.csv', 'w', newline='', encoding='utf-8') as arquivo_csv:
    writer = csv.writer(arquivo_csv)
    writer.writerow(['Nome', 'Sobrenome', 'Data de Nascimento', 'Cidade'])
    for pessoa in pessoas:
        writer.writerow(pessoa)
