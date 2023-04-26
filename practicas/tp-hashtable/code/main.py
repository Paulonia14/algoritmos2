from dictionary import *

dictionary1=createHash(9)
insert(dictionary1,5,"a")
insert(dictionary1,28,"b")
insert(dictionary1,19,"c")
insert(dictionary1,15,"d")
insert(dictionary1,20,"e")
insert(dictionary1,33,"f")
insert(dictionary1,12,"g")
insert(dictionary1,17,"h")
insert(dictionary1,10,"i")

a=search(dictionary1,10)
#Se muere con el ultimo key (10) ??
print("search:",a)

printHash(dictionary1)

delete(dictionary1,19)
delete(dictionary1,5)
asd=search(dictionary1,5)
print("search asd",asd)

print("deleted key=19 and key=5:")
printHash(dictionary1)
"""
print("------")
L=[]
L=putKeysinList(dictionary1)
printList(L)
"""
L=[0,4,15,3,5,8,1]
un=hasUniqueElements(L)
print("ej 5:",un)

