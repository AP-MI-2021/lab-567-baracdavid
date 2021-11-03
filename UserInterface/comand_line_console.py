
from Domain.vanzare2 import get_string, create_vanzare
from Logic.crud import create, delete, update


def command_line_console(vanzari):
    # add 1, Name, Gen, Price, Type
    command_line_str = input('Introduceti comanda(separator comenzi ";" iar separator paraetri ","): ')
    print('''
        exemple de comenzi:add,1,2,4,5,none;delete,1;update,1,222,422,225,silver;showall
    ''')



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
    return vanzari