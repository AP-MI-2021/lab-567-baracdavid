def show_menu():
print(
    """
        1.Adaugare o vanzare de carte
        2.
        3.
        4.
    """
)
def handle_add():
    id=input("Dati id-ul:")
    titlu=input("Dati titlu-l:")
    gen=input("Dati gen-ul:")
    pret=input("Dati pretul-ul:")
    reducere=input("Dati tipul de reducerea (none,silver,gold):")
def handle_menu():
    while True:
        show_menu()
        optiune=input("Optiunea voastra:")
        if optiune == 1: