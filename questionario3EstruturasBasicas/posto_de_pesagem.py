# Definindo a classe Queue (Fila)
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

# F: a cada F veículos, 1 é pesado
# ti = 1 se passar sem ser abordado
# ti = 5 ao passar, ser abordado e ser liberado
# ti = 10 ao passar, ser abordado e ultrapassa o peso
# Tira 2kg e retorna para o fim da fila
# => Elaborar um programa que determine o tempo total gasto para que todos os N 
# veículos passem pelo posto de pesagem da rodovia
N, F, P = [int(x) for x in input().split()] # Número de veículos, fator e peso limite

filaCaminhao = Queue()

a = [int(x) for x in input().split()]

for ai in a:
    filaCaminhao.enqueue(ai)

# Aqui, a fila está cheia
cont = 1 # contador começa em 1 mesmo, por facilidade
t_total = 0

while not filaCaminhao.isEmpty():
    peso_caminhao = filaCaminhao.dequeue()
    if cont == 1:
        if peso_caminhao <= P:
            t_total = t_total + 5 # Foi abordado e liberado
        else:
            t_total = t_total + 10 # Foi abordado e peso passou do limite
            filaCaminhao.enqueue(peso_caminhao - 2) # Retira 2kg e volta para o 
                                                    # fim da fila
    else:
        t_total = t_total + 1 # Não foi abordado

    cont = cont + 1
    if cont > F:
        cont = 1

print(t_total)