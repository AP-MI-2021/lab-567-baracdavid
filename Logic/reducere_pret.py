from Domain.vanzare2 import get_reducere, create_vanzare, get_pret, get_id, get_titlu, get_gen


def reducere_pret(lst_vanzari):
    """

    :param lst_vanzari:
    :return: o lista nous cu o reducere aplicata vanzarilor de tip silver sau gold
    """
    result = []
    for vanzare in lst_vanzari:
        if get_reducere(vanzare)=="silver":
            pret_nou = get_pret(vanzare) - (5 / 100) * get_pret(vanzare)
            result.append(create_vanzare(
                get_id(vanzare),
                get_titlu(vanzare),
                get_gen(vanzare),
                pret_nou,
                get_reducere(vanzare),
            ))
        elif get_reducere(vanzare)=="gold":
            pret_nou = get_pret(vanzare) - (10 / 100) * get_pret(vanzare)
            result.append(create_vanzare(
                get_id(vanzare),
                get_titlu(vanzare),
                get_gen(vanzare),
                pret_nou,
                get_reducere(vanzare),
            ))
        else:
            result.append(vanzare)

    return result