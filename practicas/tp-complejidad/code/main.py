import math

def MidSort(L):
  pivotpos=round(len(L)/2)
  pivot=L[pivotpos]
  menores=0
  mayores=0
  flag=False
  for i in range(0,pivotpos):
    if L[i]<pivot:
      menores+=1
    else:
      mayores+=1
  #Caso 0: La Lista ya está ordenada
  if menores==math.trunc(pivotpos/2):
    print("Lista Ordenada")
    return L
  #Caso 1: Hay más números mayores que menores al pivote en la parte izquierda de la lista
  if mayores>menores:
    for i in range(0,len(L)):
      if L[i]>pivot and i<pivotpos:
        numMayor=L[i]
        posMayor=i
      if L[i]<pivot and i>pivotpos:
        numMenor=L[i]
        posMenor=i
        flag=True
    if flag==True:
      #Reemplazo un número menor al pivote de la parte derecha en un número mayor al pivote en la parte izquierda
      L[posMayor]=numMenor
      L[posMenor]=numMayor
      return MidSort(L)
    else:
      #El pivote tiene todos números mayores a la derecha, por lo que no se puede reemplazar y quedaría así la lista
      return L
  #Caso 2: Hay mas números menores que mayores al pivote en la parte izquierda de la lista
  if menores>mayores:
    for i in range(0,len(L)):
      if L[i]<pivot and i<pivotpos:
        numMenor=L[i]
        posMenor=i
      if L[i]>pivot and i>pivotpos:
        numMayor=L[i]
        posMayor=i
        flag=True
    if flag==True:
      #Reemplazo un número mayor al pivote de la parte derecha en un número menor al pivote en la parte izquierda
      L[posMenor]=numMayor
      L[posMayor]=numMenor
      return MidSort(L)
    else:
      #El pivote tiene todos números menores a la derecha, por lo que no se puede reemplazar y quedaría así la lista
      return L
  return L 

def Contiene_Suma(A,n):
  for i in range (0,len(A)):
    for j in range (0,len(A)):
      #Suma los elementos de la lista (que no sean el mismo) y los compara con n
      if A[i]+A[j]==n and i!=j:
        return True
  return False

def printList(L):
  print("[ ", end="")
  for i in range(0,len(L)):
    print(L[i], end=" ")
  print("] ", end="")
  print("")

#--------------- Testing ---------------

L=[1,2,3,4,5,6,7,8]
L2=[2,4,8,6]
L3=[6,1,8,5,2,4]
L4=[8,1,10,9,7,2,4,11,5]
L5=[2,1,4,8,7,10,5,11,3]
L6=[5,2,4,7,8]
L7=[2,4,5,6]

L8=[5,2,2,7]
n8=4

n=1
n2=8
n3=9

a=Contiene_Suma(L,n)
print("contiene suma 1: ", a)
a2=Contiene_Suma(L2,n2)
print("contiene suma 2: ", a2)
a3=Contiene_Suma(L2,n3)
print("contiene suma 3: ", a3)
a4=Contiene_Suma(L8,n8)
print("contiene suma 3: ", a4)
print("-----------------------")

print("lista 1")
A1=MidSort(L)
printList(A1)
print("lista 2")
A2=MidSort(L2)
printList(A2)
print("lista 3")
A3=MidSort(L3)
printList(A3)
print("lista 4")
A4=MidSort(L4)
printList(A4)
print("lista 5")
A5=MidSort(L5)
printList(A5)
print("lista 6")
A6=MidSort(L6)
printList(A6)
print("Lista 7")
A7=MidSort(L7)
printList(A7)
