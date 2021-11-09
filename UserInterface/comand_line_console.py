
from Domain.vanzare2 import get_string, create_vanzare
from Logic.crud import create, delete, update
from Logic.modificare_gen import modificare_gen_dupa_titlu
from Logic.reducere_pret import reducere_pret


def command_line_console(vanzari):
    # add 1, Name, Gen, Price, Type
    print('''
           exemple de comenzi: add,1,Titlu_1,Gen_1,5,none;add,3,Titlu_3,Gen_3,5,none;
           add,20,Titlu_20,Gen_20,5,none;update,1,Titlu_1_nou,Gen_1_nou,225,silver;reducere;
           modifica_gen,Titlu_3,Gen_3_mod;showall
       ''')
    command_line_str = input('Introduceti comanda(separator comenzi ";" iar separator paraetri ","): ')



    command_lines = command_line_str.split(';')
    for index in range(0, len(command_lines)):
        command = command_lines[index].split(',')
        if command[0] == 'add':
            try:
                vanzari = create(vanzari, int(command[1]), command[2],
                             command[3], float(command[4]), command[5])
            except ValueError as ve:
                print('Eroare! Detalii: ', ve)
        elif command[0] == 'showall':
            for vanzare in vanzari:
                print(get_string(vanzare))
        elif command[0] == 'delete':
            try:
                vanzari = delete(vanzari, int(command[1]))
            except ValueError as ve:
                print('Eroare! Detalii: ', ve)
        elif command[0] == 'update':
            try:
                vanzare = create_vanzare(int(command[1]), command[2],
                                 command[3], float(command[4]), command[5])

                vanzari = update(vanzari, vanzare)
            except ValueError as ve:
                print('Eroare! Detalii: ', ve)
        elif command[0] == 'reducere':
            try:
                vanzari =reducere_pret(vanzari)

            except ValueError as ve:
                print('Eroare! Detalii: ', ve)
        elif command[0] == 'modifica_gen':
            try:
                vanzari = modificare_gen_dupa_titlu(vanzari, command[1], command[2])
            except ValueError as ve:
                print('Eroare! Detalii: ', ve)
    return vanzari