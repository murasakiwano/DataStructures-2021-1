# Forévis Alonis - Questão 3
from queue import PriorityQueue


class Grafo:
    def __init__(self, N):
        self.v = N  # Número de vértices
        self.arestas = [[-1 for i in range(N)] for j in range(N)]
        self.visitados = []

    def insere_aresta(self, u, v, peso=1):
        self.arestas[u-1][v-1] = peso
        self.arestas[v-1][u-1] = peso

    def dijkstra(self, vertice_inicial):
        D = {v: float('inf') for v in range(self.v)}
        D[vertice_inicial] = 0

        pq = PriorityQueue()
        pq.put((0, vertice_inicial))

        while not pq.empty():
            (dist, vert_atual) = pq.get()
            self.visitados.append(vert_atual)

            for vizinho in range(self.v):
                if self.arestas[vert_atual-1][vizinho-1] != -1:
                    distancia = self.arestas[vert_atual-1][vizinho-1]
                    if vizinho not in self.visitados:
                        custo_antigo = D[vizinho]
                        custo_novo = D[vert_atual] + distancia
                        if custo_novo < custo_antigo:
                            pq.put((custo_novo, vizinho))
                            D[vizinho] = custo_novo

        return D


N = int(input())
grafo = Grafo(N)

for i in range(N):
    L = input().split()
    id = int(L[0])
    A = L[1]
    vertices = [int(x) for x in L[2:]]
    if A and A != 0:
        for vertice in vertices:
            grafo.insere_aresta(id, vertice, 1)
    else:
        continue


id_o, id_d = [int(x) for x in input().split()]

D = grafo.dijkstra(id_o)

if D[id_d] != float('inf'):
    print(D[id_d] - 1)
else:
    print("Forevis alonis...")
