# Tem que fazer uma espécie de BFS colorindo um vértice
# de rubro e o adjacente de preto
from collections import defaultdict
from queue import Queue


class Vertex():
    def __init__(self, num):
        self.id = num
        self.color = None
        self.pred = None
        self.connections = []

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def setPred(self, vertice):
        self.pred = vertice

    def getPred(self):
        return self.pred

    def getConnections(self):
        return self.connections


class Graph():
    def __init__(self, verts):
        self.graph = defaultdict(list)
        self.V = verts

    def addEdge(self, u, v):
        self.graph[u].append(v)
        u.connections += [v]
        if u.getColor() == None:
            u.setColor('black')
        if u.getColor() == 'black':
            v.setColor('red')
        elif u.getColor() == 'red':
            v.setColor('black')

    def getGraph(self):
        return self.graph


n = int(input())
g = Graph(n)
verticesEArestas = []
testes = []
deuRuim = False

for _ in range(n):
    L = [int(x) for x in input().split()]

    id, A = L[:2]
    ID = Vertex(id)
    if A > 0:
        verticesEArestas += [[ID, *L[2:]]]

listaVertices = [v[0] for v in verticesEArestas]

for v in verticesEArestas:
    vert = v[0]
    for aresta in v[1:]:
        for vertice in listaVertices:
            if aresta == vertice.id:
                g.addEdge(vert, vertice)


for v in g.getGraph().keys():
    for adjacente in v.getConnections():
        if adjacente.getColor() == v.getColor():
            deuRuim = True
    testes.append(deuRuim)

if listaVertices == []:
    testes.append(False)

if False in testes:
    print('Lerei "O Vermelho e o Negro".')
else:
    print('Mais cor, por favor!')
