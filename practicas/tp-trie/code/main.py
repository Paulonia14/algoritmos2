from trie import *


T=Trie()
insert(T,"hola")
insert(T,"holanda")
insert(T,"pablo")
insert(T,"perro")
insert(T,"torta")
insert(T,"ho")

T2=Trie()
insert(T2,"pablo")
insert(T2,"holanda")
insert(T2,"perro")
insert(T2,"atrot")
insert(T2,"ho")
insert(T2,"torta")


"""
print("compare trees")

a=CompareTrees(T,T2)
print("T1 y T2",a)


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

print("Delete:")

d1=delete(T,"ho")
print("ho:",d1)
d11=search(T,"ho")
print("ho search:",d11)

d2=delete(T,"holanda")
print("holanda del:",d2)
d22=search(T,"holanda")
print("holanda search:",d22)

d5=search(T,"hola")
print("hola esta",d5)


d3=delete(T,"pablo")
print("pablo del:",d3)
d33=search(T,"pablo")
print("pablo search:",d33)

d4=search(T,"perro")
print("perro esta ",d4)


d3=delete(T,"perro")
print("perro del:",d3)
d33=search(T,"perro")
print("perro search:",d33)

asdas=search(T,"hol")
print("asds",asdas)

asdass=search(T," ")
print("adsaasa",asdass)

b=Ejercicio6(T)
print("T1",b)
"""
c=Ejercicio6(T2)
print("T2",c)

L4=[]
L4=Ejercicio4(T,"pd",5)
printListNormal(L4)

asd=autoCompletar(Trie, "ho")
print("Ej 7: ",asd)