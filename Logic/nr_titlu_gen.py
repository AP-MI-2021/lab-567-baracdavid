from Domain.vanzare2 import get_gen
from Logic.pret_min_gen import gen_list
from Tests.test_crud import get_data


def distinct_titles(vanzari):
    """
    Returneaza numarul de titluri pentru fiecare gen din vanzari
    :param vanzari: lista cu vanzari
    :return: nr_titluri: lista cu numarul de titluri pentru fiecare gen
              g: lista de genuri distincte
    """
    genuri=gen_list(vanzari)
    nr_titluri=[]
    g=[]
    for gen in genuri:
        n=0
        for vanzare in vanzari:
            if gen == get_gen(vanzare):
                n+=1
        nr_titluri.append(n)
        g.append(gen)
    return nr_titluri,g