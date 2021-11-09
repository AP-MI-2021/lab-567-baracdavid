from Domain.vanzare2 import get_pret


def ordonare_vanzari_pret(lista_vanzari):
    """

    :param lista_vanzri:
    :return: o lista noua odonata dupa pret
    """
    return sorted(lista_vanzari,key=get_pret)