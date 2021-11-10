from Domain.vanzare2 import get_string, create_vanzare, get_reducere, get_pret, get_titlu, get_gen
from Logic.crud import delete, create, update, read
from Logic.modificare_gen import modificare_gen_dupa_titlu
from Logic.nr_titlu_gen import distinct_titles
from Logic.ordonare import ordonare_vanzari_pret
from Logic.pret_min_gen import gen_list, min_price_by_gen
from Logic.reducere_pret import reducere_pret
from UserInterface.comand_line_console import command_line_console


def show_menu():
    print('1. CRUD')
    print('2. Modificarea genului pentru un titlu dat')
    print('3. Aplicarea unui discount de 5% pentru toate reducerile silver și 10% pentru toate reducerile gold')
    print('4. Ordonare Vanzari dupa pret')
    print('5. Determinarea prețului minim pentru fiecare gen.')
    print('6. Afișarea numărului de titluri distincte pentru fiecare gen')
    print('z. Undo')
    print('y. Redo')
    print('a. Afisare lista')
    print('c. Command line console')

    print('x. Exit')

def handle_add(lista_vanzari):
    id= int (input("Dati id-ul:"))
    titlu = input("Dati titlul:")
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
    id_delete = int (input("dati id-ul vanzarii pe care vreti sa o stergeti:"))
    return delete(lista_vanzari,id_delete)
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
def handle_min_price(vanzari):
    genuri=gen_list(vanzari)
    preturi_minime=min_price_by_gen(vanzari)
    for i in range(0,len(genuri)):
        print(f'Genul {genuri[i]} are pretul minim de {preturi_minime[i]}.')
def handle_nr_titluri_gen(vanzari):
    nr_titluri,genuri=distinct_titles(vanzari)
    for i in range(0,len(nr_titluri)):
        print(f'Genul {genuri[i]} are {nr_titluri[i]} titluri.')
def handle_command_console(vanzari):
    return command_line_console(vanzari)
def handle_modificare_gen_dupa_titlu(lista_vanzari):
    try:
        titlu = input('Dati titlul pentru care vreti sa modificati genul: ')
        gen= input('Dati noul gen: ')
        lista_vanzari = modificare_gen_dupa_titlu(lista_vanzari,titlu,gen)
        print('Genul a fost modificat cu succes.')
    except ValueError as ve:
        print('Eroare:', ve)

    return lista_vanzari


def handle_show_details(vanzari):
    id_vanzare = int(input("Dati id-ul vanzarii pentru care doriti detalii: "))
    vanzare = read(vanzari, id_vanzare)
    print(f'Titlul cartii: {get_titlu(vanzare)}')
    print(f'Genul cartii: {get_gen(vanzare)}')
    print(f'Pretul cartii: : {get_pret(vanzare)}')
    print(f'Tipul reducerii: {get_reducere(vanzare)}')
def handle_ordonare_pret(vanzari):
    vanzari=ordonare_vanzari_pret(vanzari)
    print('Vanzarile au fost ordonate cu succes')
    return vanzari
def handle_new_list(list_versions,current_version,vanzari):
    while current_version < len(list_versions)-1:
        list_versions.pop()
    list_versions.append(vanzari)
    current_version +=1
    return list_versions,current_version
def handle_undo(list_versions,current_version):
    if current_version < 1:
        print('Nu se mai poate face undo')
        return
    current_version -= 1
    return list_versions[current_version],current_version
def handle_redo(list_versions,current_version):
    if current_version == len(list_versions)-1:
        print('Nu se mai poate face redo')
        return
    current_version += 1
    return list_versions[current_version],current_version

def handle_crud(list_versions, current_version,vanzari):
    while True:
        try:
            print('1. Adaugare')
            print('2. Modificare')
            print('3. Stergere')
            print('a. Afisare')
            print('d. Detalii vanzare')
            print('b. Revenire')

            optiune = input('Optiunea aleasa: ')
            if optiune == '1':
                vanzari = handle_add(vanzari)
                list_versions, current_version = handle_new_list(list_versions, current_version, vanzari)
            elif optiune == '2':
                vanzari = handle_update(vanzari)
                list_versions, current_version = handle_new_list(list_versions, current_version, vanzari)
            elif optiune == '3':
                vanzari = handle_delete(vanzari)
                list_versions, current_version = handle_new_list(list_versions, current_version, vanzari)
            elif optiune == 'a':
                handle_show_all(vanzari)
            elif optiune == 'd':
                handle_show_details(vanzari)
            elif optiune == 'b':
                break
            else:
                print('Optiune invalida.')
        except Exception as ex:
            print('Eroare: ', ex)
    return vanzari,list_versions, current_version
def run_ui(vanzari):
    list_versions = [vanzari]
    current_version = 0
    while True:
        try:
            show_menu()
            optiune = input('Optiunea aleasa: ')
            if optiune == '1':
                vanzari, list_versions, current_version = handle_crud(list_versions, current_version,vanzari)
            elif optiune == '2':
                vanzari = handle_modificare_gen_dupa_titlu(vanzari)
                list_versions, current_version = handle_new_list(list_versions, current_version, vanzari)
            elif optiune == '3':
                vanzari = handle_reducere_pret(vanzari)
                list_versions, current_version = handle_new_list(list_versions, current_version, vanzari)
            elif optiune == '4':
                vanzari = handle_ordonare_pret(vanzari)
                list_versions, current_version = handle_new_list(list_versions, current_version, vanzari)
            elif optiune == '5':
                handle_min_price(vanzari)
                # list_versions, current_version = handle_new_list(list_versions, current_version, vanzari)
            elif optiune == '6':
                handle_nr_titluri_gen(vanzari)
            elif optiune == 'c':
                vanzari = handle_command_console(vanzari)
                list_versions, current_version = handle_new_list(list_versions, current_version, vanzari)
            elif optiune == 'z':
                vanzari,current_version = handle_undo(list_versions,current_version)
            elif optiune == 'y':
                vanzari,current_version = handle_redo(list_versions,current_version)
            elif optiune == 'a':
                handle_show_all(vanzari)
            # elif optiune == 'q':
            #     print("current_version",current_version)
            #     print("list_versions",list_versions)
            elif optiune == 'x':
                break
            else:
                print('Optiune invalida.')
        except Exception as ex:
            print('Eroare: ', ex)

    return vanzari
