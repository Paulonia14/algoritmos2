from trie import *


T=Trie()
insert(T,"hola")
insert(T,"holanda")
insert(T,"pablo")
insert(T,"perro")
insert(T,"torta")
insert(T,"ho")


a=search(T,"hola")
print("hola esta ",a)
b=search(T,"perro")
print("perro ",b)
c=search(T,"torta")
print("torta ",c)
d=search(T,"hol")
print("hol ",d)
e=search(T,"perrote")
print("perrote ",e)
f=search(T,"ho")
print("ho ",f )
g=search(T,"skajhdfaksfhadfñasfhaf")
print("skajhdfaksfhadfñasfhaf",g)
h=search(T,"h")
print("h",h)
