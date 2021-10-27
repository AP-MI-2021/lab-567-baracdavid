from Tests.test_crud import test_crud
from UserInterface.console import handle_menu

def main():
    lista_vanzari = []
    lista_vanzari = handle_menu(lista_vanzari)

if __name__ == '__main__':
    test_crud()
    main()