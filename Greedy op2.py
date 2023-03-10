import random
import time
import Ponderado as GRP
#import networkx as nx
import matplotlib.pyplot as plt
import heapq

lista_Heuristica = {}

def heuristica_random(nodos):
    lista_heuristica = {}
    for i in range(1,nodos+1):
        tupla_heuristica = ((i), nodos-i)
        lista_heuristica[str(i)] = tupla_heuristica
    return lista_heuristica




# Define the heuristic function
def heuristica(inicio, destino, lista):


    x1 = lista[str(inicio)][0]
    x2 = lista[str(destino)][0]
    y1 = lista[str(inicio)][1]
    y2 = lista[str(destino)][1]

    #La heuristica calculada sera la distancia entre dos puntos
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

# Define the best-first search function
def best_first_search(graph, inicio, fin, lista_Heu):
    visited = set()
    cola = [(heuristica(inicio, fin, lista_Heu), int(inicio))]
    camino = []
    i = 0
    while cola:
        (cost, nodo) = heapq.heappop(cola)
        if(i >= 1):
            nodo = nodo[0]
        #print("node: ",node)
        if nodo not in visited:
            visited.add(nodo)
            camino.append(nodo)
            if nodo == fin:
                return camino
            for neighbor in graph[str(nodo)]:
                
                heapq.heappush(cola, (heuristica(int(neighbor[0]), fin, lista_Heu) + neighbor[1], neighbor))

        i = i + 1
    return camino













def generador_grafo(nodos):
    instancia = {}
    for i in range(1,nodos+1):
        nodos_adyacentes = random.randint(2, nodos-1)
        lista_nodos_adyacentes = random.sample(range(1,nodos), nodos_adyacentes)
        while(i in lista_nodos_adyacentes):
            nodos_adyacentes = random.randint(2,nodos-1)
            lista_nodos_adyacentes = random.sample(range(1,nodos), nodos_adyacentes)
        
        lista_tuplas = []
        for j in range(0, len(lista_nodos_adyacentes)):
            lista_tuplas.append((str(lista_nodos_adyacentes[j]),random.randint(1,1000)))
        instancia[str(i)] = lista_tuplas


    for i in instancia:
        valida = 0    
        for j in instancia[i]:
            for x in instancia:
                JJ = -1
                for y in instancia[x]:
                    JJ = JJ + 1
                    if x != i:
                        if i == instancia[x][JJ][0]:
                            valida = 1
        if valida == 0:
            insertar  = str(random.randint(1, nodos))
            tupla_insertada = (i, random.randint(1,1000))
            while i == insertar:
                insertar  = str(random.randint(1, nodos))
            instancia[insertar].insert(0,tupla_insertada)

    return instancia

CantidadNodos = 10 

inicial  = str(random.randint(1, CantidadNodos))
final  = str(random.randint(1, CantidadNodos))
while inicial == final:
    inicial  = str(random.randint(1, CantidadNodos))
    final  = str(random.randint(1, CantidadNodos))

grafo = generador_grafo(CantidadNodos)
#G= nx.complete_graph(grafo)
#nx.draw_circular(G, node_size= len(grafo), width=1, width_label=False)
#plt.axes("equals")
#plt.show()

g = GRP.WeightedGraph(grafo)

print("Grafo : ", grafo)

inicio = time.time()
print(f"Inicio: {inicial}, final: {final}")
#ALGORITMO DE DIJKSTRA      -----------------------------------------------------------------------------------------------
path, weight = g.shortestPath(inicial,final)
print(f'Dijkstra: ruta: {path} peso: {weight}')

fin = time.time()
print('Tiempo de ejecucion Dijkstra: ', fin-inicio)
#--------------------------------------------------------------------------------------------------------------------------



inicio_informado = time.time()
Valores_Heuristicos = heuristica_random(CantidadNodos)
camino_informado = best_first_search(grafo, inicial, final, Valores_Heuristicos)

print(f"Camino por Algoritmo greedy informado: {camino_informado}")
fin_informado = time.time()
print('Tiempo de ejecucion Dijkstra: ', fin_informado-inicio_informado)
