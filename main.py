from Logic.crud import create
from Tests.test_crud import test_crud
from UserInterface.console import run_ui

def main():
    lista_vanzari = []
    lista_vanzari =create(lista_vanzari,1,'untitlu', 'actiune', 200, 'silver')
    lista_vanzari =create(lista_vanzari,2,'untitlu2', 'actiune2', 233, 'gold')
    lista_vanzari =create(lista_vanzari,3, 'untitlu3', 'actiune3', 1233, 'gold')
    lista_vanzari =create(lista_vanzari,4, 'untitlu4', 'actiune4', 2353, 'none')
    lista_vanzari = run_ui(lista_vanzari)

if __name__ == '__main__':
    #test_crud()
    main()