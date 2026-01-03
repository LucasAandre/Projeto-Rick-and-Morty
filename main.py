from fastapi import FastAPI
from services.rick_morty_api import RickMorty

app = FastAPI()

@app.get('/api/rickandmorty/{escolha}')
def escolha(escolha: str):

    if escolha not in ['character', 'location', 'episode']:
        return {'Erro': 'opção inválida! Use: character, location ou episode.'}
    
    informacao = RickMorty.escolha(escolha)

    return {
        'escolha': escolha,
        'personagens': informacao
    }

# BUSCA POR ID
# '/api/rickandmorty/busca/<número do ID>
# Exibir apenas o personagem do ID escolhido
# Na codificação da API, já realizar a busca na lista de personagens

@app.get('/api/rickandmorty/busca/{id}')
def busca_personagem(id: int):
    if id < 0 or id > 20:
        return {'Erro': 'Opção inválida! Digite números entre 1 e 20'}
    
    busca = RickMorty.busca_personagem(id)

    return {
        'escolha': id,
        'personagem': busca
    }
