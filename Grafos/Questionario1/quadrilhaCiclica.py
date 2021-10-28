# Detectar ciclos em um grafo

from collections import defaultdict


class Graph():
    def __init__(self, verts):
        self.graph = defaultdict(list)
        self.V = verts

    def addEdge(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]

    def ehCiclicoUtil(self, v, visited, recStack):
        # Mark current node as visited and
        # adds to recursion stack
        visited[v] = True
        recStack[v] = True

        # Recur for all neighbours
        # if any neighbour is visited and in
        # recStack then graph is cyclic
        for neighbour in self.graph[v]:
            if visited[neighbour] == False:
                if self.ehCiclicoUtil(neighbour, visited, recStack) == True:
                    return True
            elif recStack[neighbour] == True:
                return True

        # The node needs to be poped from the
        # recursion stack before the function ends
        recStack[v] = False
        return False

    # Returns true if graph is cyclic else false
    def ehCiclico(self):
        visited = {v: False for v in self.graph.keys()}
        recStack = {v: False for v in self.graph.keys()}
        for node in self.graph.keys():
            if visited[node] == False:
                if self.ehCiclicoUtil(node, visited, recStack) == True:
                    return True
        return False


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

if g.ehCiclico() == True:
    print("Hoje tem!")
else:
    print("... que ama ninguem.")
