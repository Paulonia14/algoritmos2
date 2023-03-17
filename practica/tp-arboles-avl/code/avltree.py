import mylinkedlist
import myqueue

class AVLTree:
  root = None
class AVLNode:
  parent = None
  leftnode = None
  rightnode = None
  key = None
  value = None
  bf = None

def rotateLeft(Tree,avlNode):
  #Implementa la operación rotación a la izquierda
  newNode= avlNode.rightnode
  avlNode.rightnode= newNode.leftnode
  if newNode.leftnode!=None:
    newNode.leftnode.parent=avlNode
  newNode.parent=avlNode.parent
  if avlNode.parent==None: #if avlNode == Tree.root
    Tree.root=newNode
  else:
    if avlNode.parent.leftnode==avlNode:
      avlNode.parent.leftnode=newNode
    else:
      avlNode.parent.rightnode=newNode
  newNode.leftnode=avlNode
  avlNode.parent=newNode
  return newNode
  
def rotateRight(Tree,avlNode):
  #Implementa la operación rotación a la derecha
  newNode= avlNode.leftnode
  avlNode.leftnode= newNode.rightnode
  if newNode.rightnode!=None:
    newNode.rightnode.parent=avlNode
  newNode.parent=avlNode.parent
  if avlNode.parent==None: #if avlNode == Tree.root
    Tree.root=newNode
  else:
    if avlNode.parent.leftnode==avlNode:
      avlNode.parent.leftnode=newNode
    else:
      avlNode.parent.rightnode=newNode
  newNode.rightnode=avlNode
  avlNode.parent=newNode
  return newNode

def calculateBalance(AVLTree):
  #Calcula el balance factor de un árbol binario de búsqueda
  calculateBFPerNode(AVLTree.root)
  
def calculateBFPerNode(current):
  current.bf=(calculateHeight(current.leftnode) - calculateHeight(current.rightnode))
  if current.leftnode!=None:
    calculateBFPerNode(current.leftnode)
  if current.rightnode!=None:
    calculateBFPerNode(current.rightnode)

def calculateHeight(current):
  #Saca la altura de un nodo
  if current==None:
    return 0
  elif current.leftnode==None and current.rightnode==None:
    return 1
  elif current.leftnode!=None and current.rightnode==None:
    return 1 + calculateHeight(current.leftnode)
  elif current.leftnode==None and current.rightnode!=None:
    return 1 + calculateHeight(current.rightnode)
  else:
    #compara las alturas de los hijos izquierdo y derecho y devuelve la más grande + el mismo nodo
    return 1 + max(calculateHeight(current.leftnode),calculateHeight(current.rightnode))

def calculateBFforOneNode(current):
  if current!=None:
    current.bf=(calculateHeight(current.leftnode) - calculateHeight(current.rightnode))

def traverseBreadFirstBF(AVLTree):
  #Para verificar la función calculateBalance (imprime los bf de cada nodo en amplitud)
  L=mylinkedlist.LinkedList()
  if AVLTree.root!=None:
    LR=mylinkedlist.LinkedList()
    myqueue.enqueue(L,AVLTree.root)
    while L.head!=None:
      current= myqueue.dequeue(L)
      myqueue.enqueue(LR,current.bf)
      if current.leftnode!= None:
        myqueue.enqueue(L,current.leftnode)
      if current.rightnode != None:
        myqueue.enqueue(L,current.rightnode)
    while LR.head!=None:
      aux=myqueue.dequeue(LR)
      mylinkedlist.insert(L,aux,mylinkedlist.length(L))
  return L

def reBalance(AVLTree):
  calculateBalance(AVLTree)
  BalanceTree(AVLTree,AVLTree.root)
  
def BalanceTree(AVLTree,current):
  if current.leftnode!=None:
    BalanceTree(AVLTree,current.leftnode)
  if current.rightnode!=None:
    BalanceTree(AVLTree,current.rightnode)
  if current.bf>1 or current.bf<-1:
    if current.bf>1: #rotación a la derecha
      if current.leftnode!=None and current.leftnode.bf==-1:
        rotateLeft(AVLTree,current.leftnode)
        rotateRight(AVLTree,current)
      else:
        rotateRight(AVLTree,current)
    if current.bf<-1: #rotación a la izquierda
      if current.rightnode!=None and current.rightnode.bf==1:
        rotateRight(AVLTree,current.rightnode)
        rotateLeft(AVLTree,current)
      else:
        rotateLeft(AVLTree,current)

# -------- Operaciones de binarytree adaptadas a AVL Trees --------
def search(AVLTree,element):
  if AVLTree.root==None:
    return None
  else:
    key=None
    key=searchValue(AVLTree.root,element,key)
    return key
def searchValue(current,element,key):
  #Busca un elemento en el árbol binario
  if element==current.value:
    key=current.key
    return key
  else:
    if current.leftnode!=None:
      key=searchValue(current.leftnode,element,key)
    if current.rightnode!=None:
      key=searchValue(current.rightnode,element,key)
  return key

def insert(AVLTree,element,key):
  #Inserta un elemento con una clave determinada en un AVLTree y rebalancea luego de insertar si es necesario
  newNode=AVLNode()
  newNode.value=element
  newNode.key=key
  if AVLTree.root==None:
    AVLTree.root=newNode
  else:
    keyInsert=None
    keyInsert=insertNode(newNode,AVLTree.root,keyInsert)
    reBalance(AVLTree)
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

def delete(AVLTree,element):
  #Elimina un elemento de un árbol AVL
  if AVLTree.root==None:
    return None
  elif AVLTree.root.rightnode==None and AVLTree.root.leftnode==None:
    if AVLTree.root.value==element:
      key=AVLTree.root.key
      AVLTree.root=None
      return key
    else:
      return None
  else:
    key=search(AVLTree,element)
    if key!=None:
      deletedKey=deleteKey(AVLTree,key)
      return deletedKey
    else:
      return None

def deleteKey(AVLTree,key):
  #Elimina una clave de un árbol AVL y rebalancea si es necesario
  if AVLTree.root==None:
    return None
  elif AVLTree.root.rightnode==None and AVLTree.root.leftnode==None:
    if AVLTree.root.key==key:
      AVLTree.root=None
      return key
    else:
      return None
  else:
    current=AVLTree.root
    deletedKey=None
    deletedKey=deleteNodebyKey(AVLTree,current,key,deletedKey)
    return deletedKey
def deleteNodebyKey(AVLTree,current,key,deletedKey):
  #Busco el nodo a borrar
  if key>current.key:
    if current.rightnode!=None:
      deletedKey=deleteNodebyKey(AVLTree,current.rightnode,key,deletedKey)
  elif key<current.key:
    if current.leftnode!=None:
      deletedKey=deleteNodebyKey(AVLTree,current.leftnode,key,deletedKey)
  elif key==current.key:
    deletedKey=current.key
    #Caso 1: El nodo a borrar es la raiz
    newNode=AVLNode()
    newNode=current
    if key==AVLTree.root.key:
      newNode=buscarMenordeMayores(current.rightnode)
      newNode.leftnode=current.leftnode
      newNode.rightnode=current.rightnode
      AVLTree.root=newNode
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
  reBalance(AVLTree)
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

def access(AVLTree,key):
  #Permite acceder a un elemento del árbol AVL con su clave
  current=AVLTree.root
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

def update(AVLTree,element,key):
  #Permite cambiar el valor de un elemento del árbol AVL con su clave
  newNode=AVLNode()
  newNode.value=element
  newNode.key=key
  if AVLTree.root==None:
    return None
  else:
    keyUp=None
    keyUp=updateNode(newNode,AVLTree.root,keyUp)
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

def accessBF(AVLTree,key):
  #Permite acceder al balance factor del árbol AVL con su clave
  current=AVLTree.root
  bf=None
  bf= accessBFofNode(current,key,bf)
  return bf
def accessBFofNode(current,key,bf):
  if current.key==key:
    bf=current.bf
    return bf
  if key>current.key:
    if current.rightnode!=None:
      bf=accessValue(current.rightnode,key,bf)
  elif key<current.key:
    if current.leftnode!=None:
      bf=accessValue(current.leftnode,key,bf)
  return bf