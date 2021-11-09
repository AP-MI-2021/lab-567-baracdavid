def create_vanzare (_id: int, _titlu: str, _gen: str, _pret: float, _reducere: str):
    """

    :param _id: id-ul vanzarii
    :param _titlu: titlul
    :param _gen: genul
    :param _preț: pretul vanzarii
    :param _reducere: reducerea vanzarii
    :return:
    """
    return  [
        _id,
        _titlu,
        _gen,
        _pret,
        _reducere,
    ]
def get_id(vanzare):
    return vanzare[0]

def get_titlu(vanzare):
    return vanzare[1]

def get_gen(vanzare):
    return vanzare[2]

def get_pret(vanzare):
    return vanzare[3]

def get_reducere(vanzare):
    return vanzare[4]

def get_string(vanzare):
    return f'vanzarea cu id-ul {get_id(vanzare)},cu titlul {get_titlu(vanzare)},cu genul {get_gen(vanzare)} si cu pretul {get_pret(vanzare)}'

