# Questão 9
class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()
    
    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

# Para armazenar os índices usando Deque, é remover
# o índice do fim e adicionar na frente

# Calcula o maior valor em uma lista de tamanho k
def max_k(L):
    max = L[0]
    for i in range(len(L)):
        if L[i] > max:
            max = L[i]
    
    return max

N = int(input())
L = [int(x) for x in input().split()]
k = int(input())

D = Deque()
i = 0
while (i+k) <= len(L):
        D.addFront(L[i:i+k])
        i = i + 1

# Vetor com sublistas que comportam os índices
vetorSublistas = D.items
maxLista = []

for sub in vetorSublistas:
    maxLista.append(max_k(sub))

lstr = ''
for i in range(len(maxLista)):
    lstr += str(maxLista[i]) + '  '

print(lstr.strip())