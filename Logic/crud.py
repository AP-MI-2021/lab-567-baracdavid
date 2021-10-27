from Domain.vanzare import create_vanzare, get_id

def create(lista_vanzari: list,_id: int, _titlu: str, _gen: str, _preț: int, _reducere: str):
    vanzare=create_vanzare(_id, _titlu, _gen, _preț, _reducere)
    #lista_vanzari.append(carte)
    #return lista_carti
    return  lista_vanzari + [vanzare]
def read(lista_vanzari: list, id_carte: int=None):
    vanzare_gasita=None
    for vanzare in lista_vanzari:
        if get_id(vanzare)==id_carte:
            vanzare_gasita=vanzare
    return vanzare_gasita
def update(lista_vanzari, new_sell):
    result_list=[]
    for vanzare in lista_vanzari:
        if get_id(vanzare)==get_id(new_sell):
            result_list.append(new_sell)
        else:
            result_list.append(vanzare)
    return result_list
def delete(lista_vanzari: list, id_carte: int):
    result_list=[]
    for vanzari in lista_vanzari:
        if get_id(vanzari)!=id_carte:
            result_list.append(vanzari)
    return result_list
