from Domain.vanzare2 import create_vanzare, get_id
def id_list(lst_vanzari):
    list = []
    for num in range(0, len(lst_vanzari)):
        list.append(get_id(lst_vanzari[num]))
    return list
def create(lista_vanzari: list,_id: int, _titlu: str, _gen: str, _pret: float, _reducere: str):

    #lista_vanzari.append(carte)
    #return lista_carti
    s_list = ["none", "gold", "silver"]
    if _id in id_list(lista_vanzari):
        raise ValueError('Id-ul introdus exista deja!')
    if _reducere not in s_list:
        raise TypeError('Tip reducere nerecunoscut')
    else:
        vanzare = create_vanzare(_id, _titlu, _gen, _pret, _reducere)
        return lista_vanzari + [vanzare]

def read(lista_vanzari: list, id_carte: int=None):
    vanzare_gasita=None
    for vanzare in lista_vanzari:
        if get_id(vanzare)==id_carte:
            vanzare_gasita=vanzare
    return vanzare_gasita
def update(lista_vanzari, new_sell):
    if read(lista_vanzari, get_id(new_sell)) is None:
        raise ValueError(f'Nu xista o vanzare cu id-ul {get_id(new_sell)} pe care sa o modificam.')
    result_list=[]
    for vanzare in lista_vanzari:
        if get_id(vanzare)==get_id(new_sell):
            result_list.append(new_sell)
        else:
            result_list.append(vanzare)
    return result_list
def delete(lista_vanzari: list, id_vanzare: int):
    if read(lista_vanzari, id_vanzare) is None:
        raise ValueError(f'Nu xista o vanzare cu id-ul {id_vanzare} pe care sa o modificam.')
    result_list=[]
    for vanzari in lista_vanzari:
        if get_id(vanzari)!=id_vanzare:
            result_list.append(vanzari)
    return result_list
