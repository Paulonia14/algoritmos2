def createHash(size):
  newHash=[]
  for i in range(0,size):
    newL=[]
    newHash.append(newL)
  return newHash

def hash(key,m):
  return key % m

#D = dictionary (lista)
def insert(D,key,value):
  #Inserta un key en una posición determinada por la función de hash
  #Uso la funcion hash para obtener la posición
  if D==None or key==None:
    return "Error"
  position=hash(key,len(D))
  #Creamos una tupla con key y value
  tupla=(key,value)
  if D[position]==None:
    #Si no hay nada en esa posición, va a crear una lista vacía y meter la tupla
    newList=[]
    newList.append(tupla)
    D[position]=newList
  else:
    D[position].append(tupla)

def search(D,key):
  #Busca un key en el diccionario
  position=hash(key,len(D))
  i=0
  for i in range (0,len(D[position])):
    if key==D[position][i][0]:
      return D[position][i][1]
  
def delete(D,key):
  #Elimina un key en la posición determinada por la función de hash
  position=hash(key,len(D))
  for i in range(0,len(D[position])):
    if key==D[position][i][0]:
      D[position].pop(i)
      return D


# Ejercicio 5
def uniqueElements(D):
  #devuelve True si la lista que recibe de entrada tiene todos sus elementos únicos, sino False
  for i in range(0,len(D)):
    if search(D,D[i])==True:  #??
      return False
  return True




# -- Extras --
def printHash(D):
  #Imprime toda la tabla Hash
  for i in range(0,len(D)):
    print(D[i])

def putKeysinList(D):
  # como hago
  L=[]
  for i in range(0,len(D)):
    L.append(D[i])
  return L

def printList(L):
  print("[ ", end="")
  for i in range(0,len(L)):
    print(L[i], end=" ")
  print("] ", end="")
  print("")