import pandas as pd
import requests
from datetime import datetime
import os

# Define a URL da API de cotação de moedas
url = 'https://api.exchangeratesapi.io/latest'

# Define a API key
api_key = 'kowL21dCGcIFhrITkOQKkxqPijjuS7ag'

# Define a função para obter a cotação das moedas
def get_currency_rates(api_key=None):
    # Define os parâmetros da requisição na API de cotação das moedas
    params = {}
    if api_key:
        params['access_key'] = api_key
        
    # Faz a requisição na API de cotação das moedas
    response = requests.get(url, params=params)
    # Verifica se a requisição foi bem-sucedida
    if response.status_code == 200:
        # Obtém os dados da resposta em formato JSON
        data = response.json()
        # Extrai as taxas de câmbio
        rates = data['rates']
        # Retorna as taxas de câmbio em um dicionário
        return rates
    else:
        # Retorna None se a requisição falhar
        return None

# Obtém as taxas de câmbio atuais
rates = get_currency_rates(api_key)

# Verifica se as taxas de câmbio foram obtidas com sucesso
if rates is not None:
    # Obtém a data e hora atual
    now = datetime.now()
    # Cria um DataFrame com as taxas de câmbio
    df = pd.DataFrame.from_dict(rates, orient='index', columns=['rate'])
    # Adiciona uma coluna com a data e hora da atualização
    df['timestamp'] = now
    # Define o nome do arquivo CSV e o caminho
    csv_file = 'currency_rates.csv'
    csv_path = os.path.join(os.getcwd(), csv_file)
    # Salva o DataFrame em um arquivo CSV
    df.to_csv(csv_path, mode='a', header=not os.path.exists(csv_path), index_label='currency')
    # Exibe uma mensagem de sucesso
    print(f'Taxas de câmbio salvas em {csv_file}.')
else:
    # Exibe uma mensagem de erro
    print('Não foi possível obter as taxas de câmbio.')
