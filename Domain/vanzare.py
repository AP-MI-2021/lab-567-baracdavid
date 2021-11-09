def create_vanzare (_id: int, _titlu: str, _gen: str, _pret: float, _reducere: str):
    return  {
        'id':_id,
        'titlu':_titlu,
        'gen':_gen,
        'pret':_preț,
        'reducere':_reducere,
    }
def get_id(vanzare):
    return vanzare['id']

def get_titlu(vanzare):
    return vanzare['titlu']

def get_gen(vanzare):
    return vanzare['gen']

def get_pret(vanzare):
    return vanzare['pret']

def get_reducere(vanzare):
    return vanzare['reducere']

def get_string(vanzare):
    return f'vanzarea cu id-ul {get_id(vanzare)},cu titlul {get_titlu(vanzare)},cu genul {get_gen(vanzare)} si cu pretul {get_pret(vanzare)}'

