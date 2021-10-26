from Domain.carte import get_new_book,get_titlu,get_book_string
from Logic.crud import create, update, delete
from Tests.test_crud import test_update,test_create, test_read, test_crud

carte1=get_new_book(1,"Baltagul","camedie",50,"none")
#print(get_book_string(carte1))
list=[]
list=create(list,1,"Baltagul","camedie",50,"none")
list=create(list,2,"Baltagul","camedie",50,"silver")
# print(list)
# newb=get_new_book(1,"ion","lectura",100,"none")
# list=update(list,newb)
# print(list)
# list=delete(list,2)
# print(list)
test_crud