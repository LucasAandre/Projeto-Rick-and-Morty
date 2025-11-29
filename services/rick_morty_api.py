import json
import requests

class RickMorty:

    url = 'https://rickandmortyapi.com/api'
    data_base = 'database/avaliacoes.json'
   
    @classmethod
    def personagens(cls, escolha: str):
        response = requests.get(f'{cls.url}/{escolha}')

        if response.status_code != 200:
            return {'Erro': 'Não foi possível acessar a API.'}
        
        dados = response.json()

        personagens = []

        for item in dados['results']:
            personagens.append({
                'id': item['id'],
                'nome': item['name']
            })

        return personagens
