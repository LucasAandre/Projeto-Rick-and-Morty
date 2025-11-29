from fastapi import FastAPI
from services.rick_morty_api import RickMorty

app = FastAPI()

@app.get('/api/rickandmorty/{escolha}')
def personagens(escolha: str):

    if escolha not in ['character', 'location', 'episode']:
        return {'Erro': 'opção inválida! Use: character, location ou episode.'}
    
    personagem = RickMorty.personagens(escolha)

    return {
        'escolha': escolha,
        'personagens': personagem
    }
