from Domain.vanzare import create_vanzare, get_id
from Logic.crud import create, read, update, delete


def get_data():
    return [
        create_vanzare(1, "ion", "lectura", 100, "none"),
        create_vanzare(2, "Baltag", "actiue", 70, "silver"),
        create_vanzare(3, "Ana", "Drama", 20, "gold"),
        create_vanzare(4, "Povesti", "lectura", 48, "none"),
    ]
def test_create():
    list=get_data()
    new_book =create_vanzare(6, "Baltagul", "camedie", 50, "none")
    lista_noua=create(list,6,"Baltagul","camedie",50,"none")
    assert len(lista_noua)==len(list)+1
    assert new_book in lista_noua
    #print("aici1")
def test_read():
    list=get_data()
    random_book=list[2]
    assert read(list,get_id(random_book))==random_book
def test_update():
    list=get_data()
    new_book =create_vanzare(5, "Baltagul", "camedie", 51, "none")
    lista_noua=update(list,new_book)
    assert len(lista_noua)==len(list)
    #print("ola")
def test_delete():
    list = get_data()
    id_delete=3
    deleted_book=read(list,id_delete)
    lista_noua=delete(list,id_delete)
    assert len(lista_noua)==len(list)-1
    assert deleted_book not in lista_noua
    #print("test")
def test_crud():
    test_create()
    test_read()
    test_update()
    test_delete()
