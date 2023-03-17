import mylinkedlist
from myqueue import *

class BinaryTree:
  root=None

class BinaryTreeNode:
  key=None
  value=None
  leftnode=None
  rightnode=None
  parent=None

# ------ Ejercicio 1 ------
def search(B,element):
  if B.root==None:
    return None
  else:
    key=None
    key=searchValue(B.root,element,key)
    return key
def searchValue(current,element,key):
  #Busca un elemento en el TAD árbol binario
  if element==current.value:
    key=current.key
    return key
  else:
    if current.leftnode!=None:
      key=searchValue(current.leftnode,element,key)
    if current.rightnode!=None:
      key=searchValue(current.rightnode,element,key)
  return key

def insert(B,element,key):
  #Inserta un elemento con una clave determinada
  newNode=BinaryTreeNode()
  newNode.value=element
  newNode.key=key
  if B.root==None:
    B.root=newNode
  else:
    keyInsert=None
    keyInsert=insertNode(newNode,B.root,keyInsert)
    return keyInsert
def insertNode(newNode,current,keyInsert):
  if newNode.key>current.key:
    if current.rightnode!=None:
      insertNode(newNode,current.rightnode,keyInsert)
    else:
      current.rightnode=newNode
      newNode.parent=current
  elif newNode.key<current.key:
    if current.leftnode!=None:
      insertNode(newNode,current.leftnode,keyInsert)
    else:
      current.leftnode=newNode
      newNode.parent=current
  else:
    return None
  return newNode.key

def delete(B,element):
  #Elimina un elemento del TAD árbol binario
  if B.root==None:
    return None
  elif B.root.rightnode==None and B.root.leftnode==None:
    if B.root.value==element:
      key=B.root.key
      B.root=None
      return key
    else:
      return None
  else:
    key=search(B,element)
    if key!=None:
      deletedKey=deleteKey(B,key)
      return deletedKey
    else:
      return None

def deleteKey(B,key):
  #Elimina una clave del TAD árbol binario
  if B.root==None:
    return None
  elif B.root.rightnode==None and B.root.leftnode==None:
    if B.root.key==key:
      B.root=None
      return key
    else:
      return None
  else:
    current=B.root
    deletedKey=None
    deletedKey=deleteNodebyKey(B,current,key,deletedKey)
    return deletedKey
def deleteNodebyKey(B,current,key,deletedKey):
  #Busco el nodo a borrar
  if key>current.key:
    if current.rightnode!=None:
      deletedKey=deleteNodebyKey(B,current.rightnode,key,deletedKey)
  elif key<current.key:
    if current.leftnode!=None:
      deletedKey=deleteNodebyKey(B,current.leftnode,key,deletedKey)
  elif key==current.key:
    deletedKey=current.key
    #Caso 1: El nodo a borrar es la raiz
    newNode=BinaryTreeNode()
    newNode=current
    if key==B.root.key:
      newNode=buscarMenordeMayores(current.rightnode)
      newNode.leftnode=current.leftnode
      newNode.rightnode=current.rightnode
      B.root=newNode
    #Caso 2: El nodo a borrar tiene un hijo a la izquierda
    elif current.rightnode==None and current.leftnode!=None:
      if current.parent.rightnode==current:
        current.parent.rightnode=current.leftnode
      else:
        current.parent.leftnode=current.leftnode
    #Caso 3: El nodo a borrar tiene un hijo a la derecha
    elif current.rightnode!=None and current.leftnode==None:
      if current.parent.rightnode==current:
        current.parent.rightnode=current.rightnode
      else:
        current.parent.leftnode=current.rightnode
    #Caso 4: El nodo a borrar tiene dos hijos
    elif current.rightnode!=None and current.leftnode!=None:
      newNode=buscarMenordeMayores(current.rightnode)
      #Borrar nodo
      newNode.leftnode=current.leftnode
      newNode.rightnode=current.rightnode
      if current.parent.rightnode==current:
        current.parent.rightnode=newNode
      else:
        current.parent.leftnode=newNode
    #Caso 5: El nodo a borrar no tiene hijos (es una hoja)
    else:
      if current.parent.rightnode==current:
        current.parent.rightnode=None
      else:
        current.parent.leftnode=None
  return deletedKey
  
def buscarMenordeMayores(newNode):
  #Busca el Menor de los Mayores para reemplazar en el nodo a borrar
  if newNode.leftnode!=None:
    newNode=buscarMenordeMayores(newNode.leftnode)
  #Llega al menor de los mayores
  if newNode.leftnode==None:
    #Borrar nodo de abajo
    if newNode.parent.rightnode==newNode:
      newNode.parent.rightnode=None
    else:
      newNode.parent.leftnode=None
  return newNode
    
def access(B,key):
  #Permite acceder a un elemento del árbol binario con una clave determinada
  current=B.root
  element=None
  element= accessValue(current,key,element)
  return element
def accessValue(current,key,element):
  if current.key==key:
    element=current.value
    return element
  if key>current.key:
    if current.rightnode!=None:
      element=accessValue(current.rightnode,key,element)
  elif key<current.key:
    if current.leftnode!=None:
      element=accessValue(current.leftnode,key,element)
  return element

def update(B,element,key):
  #Permite cambiar el valor de un elemento del árbol binario con una clave determinada
  newNode=BinaryTreeNode()
  newNode.value=element
  newNode.key=key
  if B.root==None:
    return None
  else:
    keyUp=None
    keyUp=updateNode(newNode,B.root,keyUp)
    return keyUp
def updateNode(newNode,current,keyUp):
  if current.key==newNode.key:
    current.value=newNode.value
    keyUp=newNode.key
    return keyUp
  elif newNode.key>current.key:
    if current.rightnode!=None:
      keyUp=updateNode(newNode,current.rightnode,keyUp)
  elif newNode.key<current.key:
    if current.leftnode!=None:
      keyUp=updateNode(newNode,current.leftnode,keyUp)
  return keyUp

# ------ Ejercicio 2 ------

def traverseInOrder(B):
  #Recorre un árbol binario en orden
  L=mylinkedlist.LinkedList()
  recorridoInOrder(L,B.root)
  return L
def recorridoInOrder(L,current):
  if current!=None:
    if current.leftnode!=None:
      recorridoInOrder(L,current.leftnode)
    mylinkedlist.insert(L,current.value,mylinkedlist.length(L))
    if current.rightnode!=None:
      recorridoInOrder(L,current.rightnode)

def traverseInPostOrder(B):
  #Recorre un árbol binario en post-orden
  L=mylinkedlist.LinkedList()
  recorridoPostOrder(L,B.root)
  return L
def recorridoPostOrder(L,current):
  if current!=None:
    if current.leftnode!=None:
      recorridoPostOrder(L,current.leftnode)
    if current.rightnode!=None:
      recorridoPostOrder(L,current.rightnode)
    mylinkedlist.insert(L,current.value,mylinkedlist.length(L))

def traverseInPreOrder(B):
  #Recorre un árbol binario en pre-orden
  L=mylinkedlist.LinkedList()
  recorridoPreOrder(L,B.root)
  return L
def recorridoPreOrder(L,current):
  if current!=None:
    mylinkedlist.insert(L,current.value,mylinkedlist.length(L))
    if current.leftnode!=None:
      recorridoPreOrder(L,current.leftnode)
    if current.rightnode!=None:
      recorridoPreOrder(L,current.rightnode)

def traverseBreadFirst(B):
  #Recorre un árbol binario en modo primero anchura/amplitud
  L=mylinkedlist.LinkedList()
  if B.root!=None:
    LR=mylinkedlist.LinkedList()
    enqueue(L,B.root)
    while L.head!=None:
      current=dequeue(L)
      enqueue(LR,current.value)
      if current.leftnode!= None:
        enqueue(L,current.leftnode)
      if current.rightnode != None:
        enqueue(L,current.rightnode)
    while LR.head!=None:
      aux=dequeue(LR)
      mylinkedlist.insert(L,aux,mylinkedlist.length(L))
  return L
  


# -- Otras cosas de arboles --

# Check Balanced Tree
def checkBalancedTree(B):
  #verifica si un árbol binario está balanceado (Retorna True si lo es, False si no)
  if B.root==None:
    return None
  else:
    check=True
    levelSub1=0;levelSub2=0
    if B.root.leftnode!=None:
      levelSub1=1
      levelSub1=checkBalance(B.root.leftnode,levelSub1)
    if B.root.rightnode!=None:
      levelSub2=1    
      levelSub2=checkBalance(B.root.rightnode,levelSub2)
    if levelSub1>levelSub2:
      if (levelSub1-levelSub2)>1:
        check=False
    else:
      if (levelSub2-levelSub1)>1:
        check=False
    return check
    
def checkBalance(current,level):
  level=checkLevelperHead(current,level)
  if current.leftnode!=None:
    level=checkBalance(current.leftnode,level)
  if current.rightnode!=None:
    level=checkBalance(current.rightnode,level)
  return level
  
def checkLevelperHead(current,level):
  #Verifica si un nodo tiene hijos a izq y derecha y suma los que tenga (solo los que sean sus hijos, no va a sumar los hijos de sus hijos)
  if current.leftnode!=None:
    level+=1
  if current.rightnode!=None:
    level+=1
  return level
 
# Check SubTree
def checkSubTree(B1,B2):
  #determina si B2 es un subárbol de B1 (Retorna True si lo es, False si no, y None si alguno de los árboles ingresados está vacío)
  #Primero verifico si el tamaño del árbol 1 es mayor al tamaño del árbol 2, luego si se ingresa algún arbol vacío
  L1=traverseBreadFirst(B1)
  L2=traverseBreadFirst(B2)
  if mylinkedlist.length(L1)<mylinkedlist.length(L2):
    print("Tamaños no válidos")
    return None
  elif B1.root==None or B2.root==None:
    return None
  else:
    check=False
    check=checkSubHead(B1.root,B2.root,check)
    return check
    
def checkSubHead(currentB1,currentB2,check):
  if currentB1!=None:
    #Encuentro donde empieza el subarbol B2, si su raiz no se encuentra en B1 delvuelve False
    if currentB1.key==currentB2.key:
      check=True
      check=checkSubTreeComplete(currentB1,currentB2,check)
      return check
    else:
      if currentB1.leftnode!=None:
        check=checkSubHead(currentB1.leftnode,currentB2,check)
      if currentB1.rightnode!=None:
        check=checkSubHead(currentB1.rightnode,currentB2,check)
  return check
  
def checkSubTreeComplete(currentB1,currentB2,check):
  #Verifico si los nodos son distintos
  if currentB1!=None and currentB2!=None:
    if currentB1.key!=currentB2.key:
      check=False
  #Checkeo si el segundo arbol tiene nodos de más por izquierda o derecha
  if currentB1.leftnode==None and currentB2.leftnode!=None:
    check=False
  elif currentB1.rightnode==None and currentB2.rightnode!=None:
    check=False
  #Checkeo si los dos arboles tienen nodos a la izquierda
  if currentB1.leftnode!=None and currentB2.leftnode!=None:
    check=checkSubTreeComplete(currentB1.leftnode,currentB2.leftnode,check)
  #Checkeo si los dos arboles tienen nodos a la derecha 
  if currentB1.rightnode!=None and currentB2.rightnode!=None:
    check=checkSubTreeComplete(currentB1.rightnode,currentB2.rightnode,check)
  return check

# Check Binary Search Tree
def checkBST(B):
  #verifica que un árbol binario es un Árbol Binario de Búsqueda (Retorna True si lo es, False si no)
  if B.root==None:
    return None
  checkBinary=True
  checkBinary=checkBTree(B.root,checkBinary)
  return checkBinary
def checkBTree(current,checkBinary):
  if current!=None:
    if current.leftnode!=None:
      if current.leftnode.key>=current.key:
        checkBinary=False
    if current.rightnode!=None:
      if current.rightnode.key<=current.key:
        checkBinary=False
    checkBinary=checkBTree(current.leftnode,checkBinary)
    checkBinary=checkBTree(current.rightnode,checkBinary)
  return checkBinary