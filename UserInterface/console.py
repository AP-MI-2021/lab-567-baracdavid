from Domain.vanzare2 import get_string, create_vanzare
from Logic.crud import delete, create, update
from Logic.modificare_gen import modificare_gen_dupa_titlu
from Logic.reducere_pret import reducere_pret


def show_menu():
    print(
        """
            1.Adaugare o vanzare de carte
            2.Sterge o vanzare
            3.Modifica o vanzare dupa id
            4.Listeaza vanzarile
            5.Aplicarea unui discount de 5% pentru toate reducerile silver și 10% pentru toate reducerile gold.
            6.Modificarea genului pentru un titlu dat.
            x.Inchide programul
        """
)
def handle_add(lista_vanzari):
    id=int(input("Dati id-ul:"))
    titlu=input("Dati titlu-l:")
    gen=input("Dati gen-ul:")
    pret=int(input("Dati pretul-ul:"))
    corect=False
    while  not corect:
        reducere = input("Dati tipul de reducerea (none,silver,gold):")
        if reducere == "none" or reducere == "silver" or reducere =="gold" :
            corect=True
            return create(lista_vanzari, id, titlu, gen, pret, reducere)
        else:
            print("reducerea nu este valida")

def handle_update(lista_vanzari):
    id_vanzare = int(input('Dati id-ul vanzarii care se actualizeaza: '))
    titlu = input('Dati noul titlu al vanzarii: ')
    gen= input('Dati nou gen al vanzarii: ')
    pret = int(input('Dati noul pret al vanzarii:'))
    corect = False
    while not corect:
        reducere = input('Dati noua reducere a vanzarii: ')
        if reducere == "none" or reducere == "silver" or reducere == "gold":
            corect = True
            vanzare=create_vanzare(id_vanzare,titlu, gen, pret, reducere)
            return update(lista_vanzari, vanzare)
        else:
            print("reducerea nu este valida")


def handle_delete(lista_vanzari):
    id_delete=int(input("dati id-ul vanzarii pe care vreti sa o stergeti:"))
    return delete(lista_vanzari,id_delete)
    print(lista_noua)
def handle_show_all(lista_vanzari):
    for vanzare in lista_vanzari:
        print(get_string(vanzare))

def handle_reducere_pret(lista_vanzari):
    try:
        vanzare = reducere_pret(lista_vanzari)

        print('Preturile au fost reduse cu succes.')
    except ValueError as ve:
        print('Eroare:', ve)

    return vanzare
def handle_modificare_gen_dupa_titlu(lista_vanzari):
    try:
        titlu = input('Dati titlul pentru care vreti sa modificati genul: ')
        gen= input('Dati noul gen: ')
        lista_vanzari = modificare_gen_dupa_titlu(lista_vanzari,titlu,gen)
        print('Genul a fost modificat cu succes.')
    except ValueError as ve:
        print('Eroare:', ve)

    return lista_vanzari
def handle_menu(lista_vanzari):
    while True:
        show_menu()
        optiune=input("Optiunea voastra:")
        if optiune == '1':
            lista_vanzari = handle_add(lista_vanzari)
        if optiune == '2':
            lista_vanzari = handle_delete(lista_vanzari)
        if optiune == '3':
            lista_vanzari = handle_update(lista_vanzari)
        if optiune == '4':
            handle_show_all(lista_vanzari)
        if optiune == '5':
            lista_vanzari = handle_reducere_pret(lista_vanzari)
        if optiune == '6':
            lista_vanzari = handle_modificare_gen_dupa_titlu(lista_vanzari)
        if optiune == 'x':
            break
    return lista_vanzari