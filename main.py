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
        'dados': informacao
    }

# BUSCA POR ID
# '/api/rickandmorty/busca/<número do ID>
# Exibir apenas o personagem do ID escolhido
# Na codificação da API, já realizar a busca na lista de personagens

@app.get('/api/rickandmorty/busca/{id}')
def busca_personagem(id: int):
    if id < 1 or id > 20:
        return {'Erro': 'Opção inválida! Digite números entre 1 e 20'}
    
    busca = RickMorty.busca_personagem(id)

    return {
        'escolha': id,
        'personagem': busca
    }

# http://127.0.0.1:8000/api/rickandmorty/1/avaliar?nota=9&comentario=Otimo+comeco
@app.get('/api/rickandmorty/{episodio}/avaliar')
def avaliar_episodio(episodio: int, nota: float, comentario: str):
    if episodio < 1 or episodio > 20:
        return {'Erro': f'Episódio {episodio} inexistente!'}

    RickMorty.nova_avaliacao(episodio, nota, comentario)

    return {
        'episodio': episodio,
        'nota': nota,
        'comentario': comentario
    }

@app.get('/api/rickandmorty/avaliacoes/{episodio}')
def listar_avaliacoes(episodio: int):
    avaliacoes = RickMorty.listar_avaliacoes(episodio)

    return {
        'episodio': episodio,
        'avaliacoes': avaliacoes
    }
