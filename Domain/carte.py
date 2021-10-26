from Domain.librarie import add_book
def get_new_book (_id: int, _titlu: str, _gen: str, _preț: int, _reducere: str):
    book = {
        'id':_id,
        'titlu':_titlu,
        'gen':_gen,
        'pret':_preț,
        'reducere':_reducere
    }
    return book
def get_id(carte):
    return carte['id']

def get_titlu(carte):
    return carte['titlu']

def get_gen(carte):
    return carte['gen']

def get_pret(carte):
    return carte['pret']

def get_reducere(carte):
    return carte['reducere']

def get_book_string(carte):
    return f'Cartea cu id-ul {get_id(carte)},cu titlul {get_titlu(carte)},cu genul {get_gen(carte)}'

