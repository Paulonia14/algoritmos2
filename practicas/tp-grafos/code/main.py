from graph import *


ListV=[0,1,2,3,4,5,6,7]
ListE=[(0,1),(0,2),(1,2),(1,3),(1,5),(2,5),(2,6),(2,4),(3,5),(3,7),(4,6),(4,7),(5,7),(6,7)]

G=createGraph(ListV, ListE)
print(G)
printGraph(G)

a=existPath(G,0,7)
print(a)

ListV2=[0,1,2,3,4,5,6,7]
ListE2=[(0,1),(0,2),(1,2),(1,3),(1,5),(2,5),(2,6),(2,4),(3,5),(4,6)]
G2=createGraph(ListV2, ListE2)
print("G2:")
print(G2)

print("is connected 1")
iscon1=isConnected(G)
print(iscon1)

print("is connected 2")
iscon2=isConnected(G2)
print(iscon2)

print("is complete:")
com1=isComplete(G)
print("com 1",com1)

print("is complete 2")
com2=isComplete(G2)
print("com2",com2)

ListV4=[1,2,3,4]
ListE4=[(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)]
G4=createGraph(ListV4, ListE4)
print(G4)

print("G4 complete")
com4=isComplete(G4)
print("comp4",com4)


ListV3=["A","B","C","D","E"]
ListE3=[("A","B"),("A","C"),("A","D"),("C","E")]
G3=createGraph(ListV3, ListE3)
print("G3:")
printGraph(G3)
print(G3)

print("is tree 1")
tr1=isTree(G)
print("tr1",tr1)

print("is tree 3")
tr3=isTree(G3)
print("tr3",tr3)

