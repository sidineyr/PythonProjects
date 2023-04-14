import csv
from faker import Faker
import random

idiomas = ['de_DE', 'pt_BR', 'en_US', 'zh_CN', 'ar_EG', 'it_IT']
fake = Faker(idiomas)

pessoas = []
for i in range(6000):
    nome = fake.first_name()
    sobrenome = fake.last_name()
    data_nascimento = fake.date_of_birth(minimum_age=18, maximum_age=80)
    cidade_nascimento = fake.city_name()
    nome_pai = fake.first_name_male() + ' ' + fake.last_name()
    nome_mae = fake.first_name_female() + ' ' + fake.last_name()
    pessoas.append([nome, sobrenome, data_nascimento, cidade_nascimento, nome_pai, nome_mae])

# salvando dados em um arquivo CSV
with open('base_dados.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Nome', 'Sobrenome', 'Data de Nascimento', 'Cidade de Nascimento', 'Nome do Pai', 'Nome da Mãe'])
    for p in pessoas:
        writer.writerow(p)
