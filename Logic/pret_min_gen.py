from Domain.vanzare2 import get_gen, get_pret
from Tests.test_crud import get_data



def gen_list(vanzari):
    """
    Returneaza o lista ce contine genurile din vanzari
    :param vanzari: lista cu vanzari
    :return: lista cu genuri distincte
    """
    lst_gen=[]
    for vanzare in vanzari:
        gen=get_gen(vanzare)
        if gen not in lst_gen:
            lst_gen.append(gen)
    return lst_gen
def min_price_by_gen(vanzari):
    """
    Returneaza o lista ce contine preturile minime pentru fiecare gen
    :param vanzari: lista cu vanzari
    :return: lista cu preturile genurilor in ordinea in care se gasesc in vanzari
    """
    list_gen=gen_list(vanzari)
    preturi_minime=[]
    for gen in list_gen:
        pret_minim=9999999
        for vanzare in vanzari:
            if gen == get_gen(vanzare):
                pret=get_pret(vanzare)
                if pret <pret_minim:
                    pret_minim=pret
        preturi_minime.append(pret_minim)
    return preturi_minime
def handle_min_price_each_genre(vanzari):
    list_gen = gen_list(vanzari)
    min_prices = min_price_by_genre(vanzari)
    for i in range(0,len(list_gen)):
        print(f'Vanzarea cu pretul cel mai mic din genul {list_gen[i]} are valoarea de {min_prices[i]} lei')