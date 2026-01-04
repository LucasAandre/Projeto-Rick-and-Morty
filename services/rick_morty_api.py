import json
import requests
import os

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
            
        return {'Erro': f'Personagem com ID {id} não encontrado.'}
    
    @classmethod
    def validacao_base_avaliacoes(cls):
        # Verifica se a pasta "database" existe
        # Se não existir, cria a pasta
        if not os.path.exists('database'):
            os.makedirs('database')

        # Verifica se o arquivo de avaliações existe
        # Se não existir, cria o arquivo
        if not os.path.exists(cls.data_base):
            # Abre o arquivo em modo escrita ('w')
            # encoding='utf-8' garante suporte a acentos
            with open(cls.data_base, 'w', encoding='utf-8') as f:
                # Cria um JSON válido vazio (lista)
                json.dump([], f)

    @classmethod
    def nova_avaliacao(cls, episodio: int, nota: float, comentario: str):
        cls.validacao_base_avaliacoes()

        with open(cls.data_base, 'r', encoding='utf-8') as arquivo:
            avaliacoes = json.load(arquivo) # Lê o arquivo e carrega a lista existente de avaliações
        
        nova_avaliacao = {
            'episodio': episodio,
            'nota': nota,
            'comentario': comentario
        }

        avaliacoes.append(nova_avaliacao)

        with open(cls.data_base, 'w', encoding='utf-8') as arquivo:
            json.dump(avaliacoes, arquivo, indent=4, ensure_ascii=False)
        
        return nova_avaliacao
    
    @classmethod
    def listar_avaliacoes(cls, episodio: int):
        cls.validacao_base_avaliacoes()

        with open(cls.data_base, 'r', encoding='utf-8') as arquivo:
            avaliacoes = json.load(arquivo)
        
        avaliacao_episodio = [a for a in avaliacoes if a['episodio'] == episodio]

        if not avaliacao_episodio:
            return {
                'episodio': episodio,
                'avaliacoes': 'Nenhuma avaliação encontrada.'
            }

        # return {
        #     'episodio': episodio,
        #     'avaliacoes': avaliacao_episodio
        # }

        return avaliacao_episodio
    