def createGraph(ListV,ListE):
  #Implementa la operación crear grafo
  #V= Vertices E=Edges(Aristas)(tuplas)
  LAdj=[]
  for i in range(len(ListV)):
    #Lista Auxiliar
    LAux=[]
    LAux.append(ListV[i])
    for each in ListE:
      #Compara el primer elemento de la dupla actual con el vertice
      if each[0]==LAux[0]:
        LAux.append(each[1])
      if each[1]==LAux[0]:
        #Compara el segundo elemento de la dupla actual con el vertice
        LAux.append(each[0])
    LAdj.append(LAux)
  return LAdj


def existPath(graph,v1,v2):
  #busca si existe un camino entre los vértices v1 y v2
  BFSList=BFS(graph,v1)
  if v2 in BFSList:
    return True
  else:
    return False


def isConnected(graph):
  #Implementa la operación es conexo 
  BFSList=BFS(graph,graph[0][0])
  #BFS devuelve todos los vertices que conectan con el que le mandamos(graph[0][0])
  for each in graph:
    if each[0] not in BFSList:
      #each[0] son los vértices que hay en el grafo, si alguno no llega a estar en esa lista que conectan al vértice "inicial", entonces no es conexo
      return False
  return True


def isTree(graph):
  #Implementa la operación es árbol
  if isConnected(graph)==False:
    return False
  #Que tenga v-1 aristas(siendo v los vértices) garantiza que no tenga ciclos
  #len(graph) es igual al número de vertices(n)
  if numberEdges(graph)==len(graph)-1:
    return True
  else:
    return False


def isComplete(graph):
  #Implementa la operación es completo
  #Todos los vertices son de mismo grado
  gradeList=[]
  for each in graph:
    cont=0
    for i in range(len(each)):
      cont+=1
    gradeList.append(cont)
  #Verifica si todos los elementos de la lista son iguales (lo cual significa que los vertices tienen mismo grado)
  if len(set(gradeList)) == 1:
    return True
  else:
    return False

"""
def convertTree(graph):
  #Implementa la operación es convertir a árbol (isTree=False, entonces lo convierto en Tree)
  #evuelve una lista de aristas que si se eliminan el grafo se convierte en un árbol
  if isTree(graph)==True:
    print("No se necesitan eliminar aristas")
    return None
  eliminateEdges=[]
  queue=[]
  queue.append(graph[0][0])
  visited=[]
  visited.append(graph[0][0])
  aux=[]

  while len(queue)>0:
    positionVertex=searchVertex(graph,queue[0])
    queue.pop(0)
    for each in graph[positionVertex]:
      print(each)
      if each!=graph[positionVertex][0]:
        if each in visited:
          aux.append(each)
          print("each in cond",each)
        if each not in visited:
          visited.append(each)
          queue.append(each)
        #else:
          #aux.append(each)
          #visited.append(each)
          #print("each in cond",each)

          #if each==graph[positionVertex]:
            #t=(graph[positionVertex],each)
            #print("each",each)
            #eliminateEdges.append(t)

  print(aux)
  print(visited)
  return eliminateEdges
"""


# --------- Extras ---------

def printGraph(graph):
  for each in graph:
    print(each[0],end=" = ")
    for i in range(1,len(each)):
      if i==len(each)-1:
        print(each[i], end=" )")
      else:
        if i==1:
          print("(",each[i], end=", ")
        else:
          print(each[i], end=", ")
    print("")
      

def BFS(graph,Vstart):
  #O(|V|+|E|)
  #queue
  BFSList=[]
  queue=[]
  visited=[]
  visited.append(Vstart) #Gray Vertex
  BFSList.append(Vstart) #Black Vertex
  queue.append(Vstart)
  while len(queue)>0:
    positionVertex=searchVertex(graph,queue[0])
    queue.pop(0)
    for each in graph[positionVertex]:
      if each!=graph[positionVertex][0]:
        if each not in visited:
          visited.append(each)
          queue.append(each)
          BFSList.append(each)
  #print(BFSList)
  return BFSList
      

def searchVertex(graph,vertex):
  #Devuelve each index (graph[i])
  for i in range(len(graph)):
    if graph[i][0]==vertex:
      return i


def numberEdges(graph):
  #la cantidad de aristas es igual a la suma de los grados de todos los vértices / 2
  contEdges=0
  for each in graph:
    for i in range(1,len(each)):
      contEdges+=1
  return contEdges/2