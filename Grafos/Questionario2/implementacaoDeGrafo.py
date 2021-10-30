# Questão 3 - Implementação de Grafo


class Grafo():
    def __init__(self):
        self.vertices = []
        self.arestas = []

    def insere_v(self, id, dado):
        for vertice in self.vertices:
            if id in vertice:
                self.vertices[self.vertices.index(vertice)] = (id, dado)
                return
        self.vertices.append((id, dado))

    def insere_a(self, id_o, id_d):
        vertice_o = list(filter(lambda x: x[0] == id_o, self.vertices))
        vertice_d = list(filter(lambda x: x[0] == id_d, self.vertices))
        if vertice_o and vertice_d:
            self.arestas.append((vertice_o[0][0], vertice_d[0][0]))
            # self.arestas[vertice_d[0][0]] += [vertice_o[0][0]]

    def remove_v(self, id):
        for v in self.vertices:
            if v[0] == id:
                self.vertices.remove(v)
        self.arestas = list(filter(lambda x: id not in x, self.arestas))

    def remove_a(self, id_o, id_d):
        for aresta in self.arestas:
            if aresta == (id_o, id_d):
                self.arestas.remove((id_o, id_d))

    def grau_saida(self, id):
        return self.grau_aux(id, 0)

    def grau_entrada(self, id):
        return self.grau_aux(id, 1)

    def grau_aux(self, id, index):
        counter = 0
        for aresta in self.arestas:
            if aresta[index] == id:
                counter += 1

        return counter

    def alcancavel(self, u, v):
        for aresta in self.arestas:
            if aresta == (u, v):
                return True
        return False


n = int(input())
grafo = Grafo()

for _ in range(n):
    s = input().split()
    if len(s) == 2:
        comando, info1 = s[0], s[1]
        info2 = None
    elif len(s) == 3:
        comando, info1, info2 = s[0], s[1], s[2]

    if comando == 'IV':
        grafo.insere_v(info1, info2)
    elif comando == 'IA':
        grafo.insere_a(info1, info2)
    elif comando == 'RV':
        grafo.remove_v(info1)
    elif comando == 'RA':
        grafo.remove_a(info1, info2)

print(f'Os vértices são {grafo.vertices}')
print(f'As arestas são {grafo.arestas}')

print(grafo.grau_saida('A'), grafo.grau_entrada('A'), grafo.grau_saida(
    'B'), grafo.grau_entrada('B'), grafo.grau_saida('C'), grafo.grau_entrada('C'))
print(grafo.alcancavel('C', 'B'), grafo.alcancavel(
    'A', 'C'), grafo.alcancavel('C', 'A'))
