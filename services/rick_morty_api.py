import json
import requests

class RickMorty:

    url = 'https://rickandmortyapi.com/api'
    data_base = 'database/avaliacoes.json'
   
    @classmethod
    def escolha(cls, escolha: str):
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

    @classmethod
    def busca_personagem(cls, id: int):
        escolha = 'character'
        personagens = cls.escolha(escolha)
        
        personagem = next((p for p in personagens if p['id'] == id), None)

        if personagem:
            return personagem
            
        return {'erro': f'Personagem com ID {id} não encontrado.'}
