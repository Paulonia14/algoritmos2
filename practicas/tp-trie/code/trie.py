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
            #si la lista children tiene más de un nodo entonces no tengo que borrar el 
            # nodo current porque desvinculo el otro elemento de la lista children
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


def Ejercicio4(T,p,n):
  #dado un árbol Trie T, un patrón p y un entero n, escribe todas la palabras del árbol
  # que empiezan por p y sean de longitud n
  if T.root==None or p==None or n==None:
    return
  #Para que no haya problemas hacemos que la cadena sea en mayusculas
  p=p.upper()
  ListTree=[]
  ListTree=ListOfTreeWords(T.root.children,ListTree,"")
  correctwords=[]
  #Creamos otra lista igual
  correctwords=ListTree.copy()
  #comparar las palabras con p y n e ir sacandolas en la lista resultante
  for word in ListTree:
    for i in range(0,len(p)):
      if word[i]!=p[i]:
        correctwords.remove(word)
        break
      else:
        if len(word)!=n:
          correctwords.remove(word)
          break
  return correctwords   


#Ejercicio 5
def CompareTrees(T1,T2):
  #analizar si todas las palabras del árbol Trie T1 se encuentran en el árbol T2.
  if T1.root==None or T2.root==None:
    #Alguno de los árboles no existe
    return False
  # Pongo todas las palabras de los trie en 2 listas distintas
  T1List=[]
  T1List=ListOfTreeWords(T1.root.children,T1List,"")
  T2List=[]
  T2List=ListOfTreeWords(T2.root.children,T2List,"")
  #printListNormal(T1List)
  #printListNormal(T2List)
  #ordeno las listas
  T1List.sort()
  T2List.sort()
  if T1List==T2List:
    #Comparo las listas para ver si son iguales(implica que tienen las mismas palabras)
    return True
  else:
    return False


def Ejercicio6(T):
  #Devuelve True si existen en el documento T dos cadenas invertidas. (ejemplo abcd y dcba)
  L1=[]
  L2=[]
  #Coloco las palabras del Trie en dos listas
  L1=ListOfTreeWords(T.root.children,L1,"")
  L2=ListOfTreeWords(T.root.children,L2,"")
  for i in range(0,len(L2)):
    #Doy vuelta las palabras de la segunda lista
    L2[i]=L2[i][::-1]
  #printListNormal(L1)
  #printListNormal(L2)
  #comparo todas las palabras de la primera lista con todas de la segunda
  for word1 in L1:
    for word2 in L2:
      if word1==word2:
        return True
  return False




# ---- Extras ----
def printList(L):
  print("[ ", end="")
  for i in range(0,len(L)):
    print(L[i].key, end=" ")
  print("] ", end="")
  print("")

def printListNormal(L):
  print("[ ", end="")
  for i in range(0,len(L)):
    print(L[i], end=" ")
  print("] ", end="")
  print("")


def ListOfTreeWords(currentL,L,word):
  #Funcion para poner cada palabra de un Trie en una lista (cada elemento de la lista es una palabra)
  #Le paso T.root.children (currentL)
  for current in currentL:
    if current.children!=None:
      if len(current.children)>1:
        for child in current.children:
          word=word+current.key
          L=ListOfTreeWords([child],L,word)
          word=""
      else:
        word=word+current.key
        if current.isEndOfWord==True:
          L.append(word)
        L=ListOfTreeWords(current.children,L,word)
        word=""
    else:
      word=word+current.key
      L.append(word)
  return L