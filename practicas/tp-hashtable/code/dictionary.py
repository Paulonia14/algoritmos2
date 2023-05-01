def createHash(size):
  newHash=[]
  for i in range(0,size):
    newL=[]
    newHash.append(newL)
  return newHash

def hash(key,m):
  #Función de Hash usada
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

#Ejercicio 4
def isPermutation(cadenaS,cadenaP):
  if len(cadenaS)!=len(cadenaP):
    #Si son de distinta longitud la cadenaP no puede ser una permutacion
    return False
  size=len(cadenaS)
  D=createHash(size)
  for each in cadenaS:
    #Meto los elementos de la primera cadena en un dictionary
    insert(D,ord(each),each)
  for each in cadenaP:
    #Busco los elementos de la segunda cadena en el dictionary
    sameV=search(D,ord(each))
    if sameV==None:
      return False
  return True

# Ejercicio 5
def hasUniqueElements(L):
  #devuelve True si la lista que recibe de entrada tiene todos sus
  # elementos únicos, sino False
  D=createHash(len(L))
  #Creo un dictionary y voy metiendo valores de la lista en él, 
  # para buscarlos en ese hash para ver si ya están. Si están, retorna False, sino True.
  for i in range(0,len(L)):
    sameV=search(D,L[i])
    insert(D,L[i],L[i])
    if sameV!=None and sameV==L[i]:
      return False
  return True

#Ejercicio 6
def hashPostales(key,m):
  #los códigos postales son de la forma cddddccc (c=caracter; d=dígito)
  #ord() para dar el ascii de un valor
  return ( ord(key[0])*(10**7) + key[1]*(10**6) + key[2]*(10**5) + key[3]*(10**4) + key[4]*(10**3) + ord(key[5])*(10**2) + ord(key[6])*10 + ord(key[7]) ) % m


#Ejercicio 7
def compressedString(cadena):
  if len(cadena)==0:
    #No hay cadena
    return
  newcadena="";cont=0
  for i in range(len(cadena)):
    if i+1==len(cadena):
      cont+=1
      newcadena=newcadena+(cadena[i]+str(cont))
    else:  
      if cadena[i]==cadena[i+1]:
        cont+=1
      else:
        cont+=1
        newcadena=newcadena+(cadena[i]+str(cont))
        cont=0
  if len(newcadena)>len(cadena):
    return cadena
  return newcadena


#Ejercicio 8
def stringOccurrence(cadenaA,cadenaP):
  #Solución por hash (O(K*L))
  position=None
  if len(cadenaA)<len(cadenaP):
    return None
  if cadenaA==cadenaP:
    return 0
  D=createHash(len(cadenaA))
  for i in range(len(cadenaA)):
    #la key va a ser el valor ascii del elemento y el elemento va a ser una tupla con el elemento y la posición que le corresponde en la cadena
    t=(cadenaA[i],i)
    insert(D,ord(cadenaA[i]),t)
  printHash(D)
  flag=False
  for i in range(len(cadenaP)):
    t=search(D,ord(cadenaP[i]))
    if t[0]==cadenaP[i]:
      #Compara el primer elemento de la tupla (el cual es el elemento de la cadena) y si son iguales devuelve el segundo elemento de la tupla (el cual es la posición que tiene en su cadena)
      if flag==False:
        flag=True
        position= t[1]
    else:
      return None
  return position

def stringOcurrenceWithList(cadenaA,cadenaP):
  pass


#Ejercicio 9
def isSubset(S,T):
  #Determina si el conjunto S es subconjunto de T
  #S es subconjunto de T si todos sus elementos están en T
  D=createHash(len(T))
  for each in T:
    #Creo un hash con el conjunto T
    insert(D,each,each)
  for each in S:
    #Verifico si los elementos de S estan en T con la función search
    if search(D,each)==None:
      return False
  return True

# -- Extras --
def printHash(D):
  #Imprime toda la tabla Hash
  for i in range(0,len(D)):
    print(f"[{i}] -> {D[i]}")


def printList(L):
  print("[ ", end="")
  for i in range(0,len(L)):
    print(L[i], end=" ")
  print("] ", end="")
  print("")