#from algo1 import input_int

class LinkedList:
  head=None
  
class Node:
  value=None
  nextNode=None

def add(L,element):
  #Agrega un elemento al comienzo de la lista
  nodeHead=Node()
  nodeHead.value=element
  current=L.head
  L.head=nodeHead
  if (current==None):
    L.head=nodeHead
  else:
    nodeHead.nextNode=current
    L.head=nodeHead

def search(L,element):
  #Busca un elemento de la lista
  current=L.head
  position=0
  while current!=None:
    if current.value==element:
      return position
    position+=1
    current=current.nextNode
  return None

def insert(L,element,position):
  #Inserta un elemento en una posición determinada de la lista
  cont=0
  current=L.head
  while current!=None:
    cont+=1
    current=current.nextNode
  if (position>cont) or (position<0):
    return None
  if (position==0):
    add(L,element)
    return position
  newNode=Node()
  newNode.value=element
  current=L.head
  for i in range(0,position-1):
    current=current.nextNode
  newNode.nextNode=current.nextNode
  current.nextNode=newNode
  return position

def delete(L,element):
  #Elimina un elemento de la lista
  position=search(L,element)
  current=L.head
  if (position==None):
    return None
  if (position==0):
    L.head=current.nextNode
  else:
    for i in range (0,position-1):
      current=current.nextNode
    current.nextNode=current.nextNode.nextNode
  return position

def length(L):
  #Calcula el número de elementos de la lista
  current=L.head
  cont=0
  while current!=None:
    cont+=1
    current=current.nextNode
  return cont

def access(L,position):
  #Permite acceder a un elemento de la lista en una posición determinada
  current=L.head
  cont=length(L)
  if (position>=cont) or (position<0):
    return None
  for i in range (0,cont):
    if (i==position):
      return current.value
    current=current.nextNode
  
def update(L,element,position):
  #Permite cambiar el valor de un elemento de la lista en una posición determinada
  cont=length(L)
  if (position>cont) or (position<0):
    return None
  current=L.head
  for i in range(0,cont):
    if (position==i):
      current.value=element
    current=current.nextNode
  return position

def printList(L):
  #Imprimir la lista en pantalla
  current=L.head
  print("[ ", end="")
  while current!=None:
    print(current.value,end=" ")
    current=current.nextNode
  print("]",end="")
  print("")

def llenarLista(L):
  size=input_int("Ingrese la cantidad de elementos de la lista: ")
  for i in range(0,size):
    element=input_int(f"Elemento {i} de la lista: ")
    insert(L,element,i)

def move(L,posInicio,posFinal):
  #Mover un nodo de un lugar(posInicio) a otro(posFinal)
  element=access(L,posInicio)
  size=length(L)
  if posInicio>=size or posFinal>=size:
    return print("Posiciones no válidas")
  if posInicio>posFinal:
    initialPosition=posInicio
    finalPosition=posFinal
  elif posInicio<posFinal:
    initialPosition=posInicio-1
    finalPosition=posFinal+1
  else:
    return
  insert(L,element,finalPosition)
  current=L.head
  if posInicio==0:
    L.head=current.nextNode
  else:
    for i in range (0,initialPosition):
      current=current.nextNode
    current.nextNode=current.nextNode.nextNode

def listaOrdenada(L,posInicio,posFinal):
  #Ordena la lista ingresada de menor a mayor elemento
  #Caso base
  if posFinal==length(L)-1:
    return
  #Mover el current a la posición de destino
  current=L.head
  if posFinal!=0:
    for i in range (0,posFinal):
      current=current.nextNode
  #Buscar valor más chico
  menor=current.value
  position=posFinal
  for i in range(posFinal,length(L)):
    if current.value<=menor:
      menor=current.value
      posInicio=position
    position+=1
    current=current.nextNode
  #Mover un nodo de un lugar(posInicio) a otro(posFinal)
  element=access(L,posInicio)
  current=L.head
  if posFinal!=0:
    for i in range (0,posFinal):
      current=current.nextNode
  if (posInicio!=posFinal):
    for i in range (posFinal,posInicio-1):
      current=current.nextNode
    current.nextNode=current.nextNode.nextNode
    insert(L,element,posFinal)
  return listaOrdenada(L,posInicio,posFinal+1)

def deletePosition(L,position):
  #Elimina un elemento de la lista de acuerdo a su posición
  #Retorna el elemento eliminado
  element=access(L,position)
  current=L.head
  if (position==None):
    return None
  if (position==0):
    L.head=current.nextNode
  else:
    for i in range (0,position-1):
      current=current.nextNode
    current.nextNode=current.nextNode.nextNode
  return element