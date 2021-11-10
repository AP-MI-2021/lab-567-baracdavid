from Domain.vanzare2 import get_pret, get_id, get_gen
from Logic.crud import delete
from Logic.modificare_gen import modificare_gen_dupa_titlu
from Logic.nr_titlu_gen import distinct_titles
from Logic.ordonare import ordonare_vanzari_pret
from Logic.pret_min_gen import min_price_by_gen
from Logic.reducere_pret import reducere_pret
from Tests.test_crud import get_data


def test_reducere_pret():
    lista = get_data()
    lista = reducere_pret(lista)
    assert get_pret(lista[0]) == 100
    assert get_pret(lista[1]) == 66.5
    assert get_pret(lista[2]) == 18.0

def test_min_price_by_gen():
    lista = get_data()
    preturi_minime = min_price_by_gen(lista)
    assert preturi_minime[0] == 48
def test_ordonare():
    lista = get_data()
    new_list = ordonare_vanzari_pret(lista)
    assert get_id(new_list[0]) == 3
    assert get_id(new_list[1]) == 5
    assert get_id(new_list[2]) == 2
def test_modificare_gen_dupa_titlu():
    lista = get_data()
    lista_noua=modificare_gen_dupa_titlu(lista,'Ana','gen_nou')
    assert get_gen(lista[2]) != get_gen(lista_noua[2])
def test_distinct_titles():
    lista=get_data()
    nr_titluri,genuri=distinct_titles(lista)
    assert nr_titluri[0] == 2
    assert nr_titluri[1] == 1
    assert genuri[0] == 'lectura'
# def test_undo():
#     list_versions=[]
#     lista=get_data()
#     list_versions.append(lista)
#     curent_version=0
#     lista_noua=delete(lista,1)
#     list_versions.append(lista_noua)




def test_all():
    test_reducere_pret()
    test_min_price_by_gen()
    test_ordonare()
    test_modificare_gen_dupa_titlu()
    test_distinct_titles()
test_all()