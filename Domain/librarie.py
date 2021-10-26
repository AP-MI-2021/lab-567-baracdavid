lista_carti=[]
def get_all_books ():
    return  lista_carti
def add_book (_id:int, _titlu:str, _gen:str, _preț:int, _reducere:str):
    book = {
        'id':_id,
        'titlu':_titlu,
        'gen':_gen,
        'pret':_preț,
        'reducere':_reducere
    }
    lista_carti.append(book)