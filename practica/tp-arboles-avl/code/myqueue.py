from mylinkedlist import *

def enqueue(Q,element):
  #Agrega un elemento al comienzo de la cola Q
  add(Q,element)

def dequeue(Q):
  #Extrae el último elemento de la cola Q
  size=length(Q)
  if (size==0):
    return None
  elif (size==1):
    element=Q.head.value
    Q.head=None
  else:
    current=Q.head
    for i in range(0,size):
      if (i==size-2):
        element=current.nextNode.value
        current.nextNode=None
      else:
        current=current.nextNode
  return element
      