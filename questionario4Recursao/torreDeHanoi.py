# Questão 1 - Torre de Hanoi
# Input: N A C B
# N é o número de discos
# A é o pole inicial
# C é o pole final
# B é o pole intermediário
N, A, C, B = input().split()

N = int(N)

def moverTorre(altura, origem, destino, intermediario):
    if altura >= 1:
        moverTorre(altura-1, origem, intermediario, destino)
        moverDisco(origem, destino)
        moverTorre(altura-1, intermediario, destino, origem)

def moverDisco(origem, destino):
    print(f"Mover de {origem} para {destino}.")

moverTorre(N, A, C, B)