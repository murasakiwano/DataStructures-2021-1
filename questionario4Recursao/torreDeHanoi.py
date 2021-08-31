# Questão 1 - Torre de Hanoi
# Input: N A C B
# N é o número de discos\
N, origem, destino, intermediario = input().split()

N = int(N)

def moverTorre(altura, origem, destino, intermediario):
    if altura >= 1:
        moverTorre(altura-1, origem, intermediario, destino)
        moverDisco(origem, destino)
        moverTorre(altura-1, intermediario, destino, origem)

def moverDisco(origem, destino):
    print(f"Mover de {origem} para {destino}.")

moverTorre(N, origem, destino, intermediario)