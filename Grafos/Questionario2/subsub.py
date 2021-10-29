# Detectar se um grafo é subgrafo do outro
from collections import defaultdict


class Graph():
    def __init__(self, verts):
        self.graph = defaultdict(list)
        self.V = verts

    def addEdge(self, u, v):
        self.graph[u].append(v)


def subgrafo(g1, g2):
    for vertice in g2.graph.keys():
        if vertice not in g1.graph.keys():
            return False
        else:
            for aresta in g2.graph[vertice]:
                if aresta not in g1.graph[vertice]:
                    return False
    
    return True

grafos = []

# Agora começa o programa de fato
n = int(input())
g = Graph(n)

for _ in range(n):
    L = input().split()
    id, A = L[0], L[1]
    vertices = L[2:]
    if not vertices:
        g.graph[id] = []
    else:
        for v in vertices:
            g.addEdge(id, v)
grafos.append(g)

input()

n = int(input())
g = Graph(n)

for _ in range(n):
    L = input().split()
    id, A = L[0], L[1]
    vertices = L[2:]
    if not vertices:
        g.graph[id] = []
    else:
        for v in vertices:
            g.addEdge(id, v)
grafos.append(g)


# print(grafos[0].graph, grafos[1].graph)

# Se g[1] é subgrafo de g[0]
if subgrafo(grafos[0], grafos[1]):
    print("Sub-sub!")
else:
    print("Ue? Ue? Ue?")
