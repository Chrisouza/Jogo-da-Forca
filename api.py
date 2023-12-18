import requests


def getRandomApi():
    try:
        # URL base da API do Dicionário Aberto
        base_url = "https://api.dicionario-aberto.net/"
        # Endpoint para obter todas as palavras
        endpoint = "random"
        # Fazendo a requisição GET para obter todas as palavras
        response = requests.get(base_url + endpoint)
        # Verificando se a requisição foi bem-sucedida e obtendo os dados
        if response.status_code == 200:
            palavras = response.json()
            return palavras['word']
    except:
        return False
