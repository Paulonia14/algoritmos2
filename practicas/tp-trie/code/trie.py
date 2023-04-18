class Trie:
  root = None
class TrieNode:
  parent = None
  children = None
  key = None
  isEndOfWord = False

# ---- Ejercicio 1 ----

def insert(T, element):
  #insertar un elemento en T, siendo T un Trie.
  if element==None:
    #No se ingresó palabra a insertar
    return
  if T.root==None:
    #No hay Tree, se crea uno
    newRoot=TrieNode()
    newRoot.key=" "
    T.root=newRoot
  index=0; charIndex=0
  insertElement(T.root,element,index,charIndex)

def insertElement(current,element,index,charIndex):
  if charIndex==len(element):
    #ya cubrí toda la palabra
    current.isEndOfWord=True
    return
  if current.children==None:
    #Compruebo que el children no sea ya una lista creada (para no resetearla)
    current.children=[]
  else:
    #Para checkear si inserta
    printList(current.children)
  for i in range(0,len(current.children)):
    if current.children[i].key==element[charIndex]:
      #Comparo el caracter actual con los elementos del current.children, si 
      # son iguales vuelvo a llamar a la función
      index=i
      insertElement(current.children[i],element,index,charIndex+1)
      return
  #No son iguales
  newNode=TrieNode()
  newNode.key=element[charIndex]
  newNode.parent=current
  current.children.append(newNode)
  index=len(current.children)-1
  charIndex+=1
  #Para checkear si inserta (2)
  printList(current.children)
  insertElement(current.children[index],element,index,charIndex)

def search(T,element):
  #Verifica que un elemento se encuentre dentro del Trie.
  if T.root==None:
    #Arbol vacío
    return False
  if element==None:
    #Palabra vacía
    return False
  index=0
  check=False
  check=searchWord(T.root.children,element,index,check)
  return check

def searchWord(current,element,index,check):
  if index<len(element):
    #Evita que se rompa si busco una palabra mas chica que las que ya hay en el árbol
    if current!=None:
      for i in range(0,len(current)):
        if current[i].key==element[index]:
          #Comparo a ver si son iguales
          if (current[i].isEndOfWord==True) and (index==len(element)-1):
            #Ya cubrí la palabra
            check=True
            return check
          return searchWord(current[i].children,element,index+1,check)
      return check
    else:
      return check
  else:
    return check

def delete(T,element):
  element=element.upper()
  if search(T,element)==False:
    #No se encuentra la palabra dentro del árbol asi que retorna Falso
    print("Element not Found")
    return False
  charIndex=0
  deleteElement(T.root,element,charIndex)
  return True


def deleteElement(current,element,charIndex):
  #Current = Node
  for i in range(0,len(current.children)):
    if current.children[i].key==element[charIndex]:
      if current.children[i].isEndOfWord==True and charIndex==len(element)-1:
        if current.children[i].children!=None:
          #Si llego al fin de palabra pero la palabra a eliminar tiene hijos
          current.children[i].isEndOfWord= False
        else:
          if len(current.children)>1:
            #si la lista children tiene más de un nodo entonces no tengo que borrar el nodo current porque desvinculo el otro elemento de la lista children
            current.children.pop(i)
            return
          else:
            return unlink(current,element,charIndex)
        return
      deleteElement(current.children[i],element,charIndex+1)
      return
  return

def unlink(current,element,charIndex):
  #Current = Node
  for i in range (0,len(current.children)):
    if current.children[i].key==element[charIndex]:
      if len(current.children)>1:
        current.children.pop(i)
        return
      current.children.pop(i)
      if current.isEndOfWord==True:
        return
  unlink(current.parent,element,charIndex-1)



# ---- Extras ----
def printList(L):
  print("[ ", end="")
  for i in range(0,len(L)):
    print(L[i].key, end=" ")
  print("] ", end="")
  print("")
