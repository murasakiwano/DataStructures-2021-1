# Ordenar n números em função de um fator k
# A ordem é decrescente em relação ao módulo do número por k
# key=lambda x: -mod(x, k)
def modulo(x, k):
    if x < 0:
        return - (abs(x) % k)
    else:
        return x % k

def maior(x1, x2, k):
    # print(f"Escolhendo entre {x1} e {x2}")
    m1 = modulo(x1, k)
    m2 = modulo(x2, k)
    escolhido = None
    if m1 != m2:
        # print(f"x1={x1}, x2={x2}")
        # print(f"m1={m1}, m2={m2}")
        if m1 > m2:
            escolhido = x1
        else:
            escolhido = x2
    else:
        if (x1 % 2 == 0):
            if (x2 % 2 != 0):
                escolhido = x1
            else:
                escolhido = max(x1, x2)
        else:
            if (x2 % 2 != 0):
                escolhido = min(x1, x2)
            else:
                escolhido = x2

    # print(f"O escolhido é {escolhido}")
    return escolhido

def printLista(lista):
    strPrint = ''
    for i in range(len(lista)-1):
        strPrint += str(lista[i]) + ' '
    
    strPrint += str(lista[-1])

    print(strPrint)

def troca(vetor, a, b):
    '''Troca os conteúdos dos inteiros.'''
    vetor[a], vetor[b] = vetor[b], vetor[a]

def insertion_sort(lista):
    for i in range(1, len(lista)):
        aux = lista[i]
        j = i - 1
        # Mova os elementos da lista [0...i-1]
        # que são maiores que o elemento comparado
        # para uma posição à frente da sua posição atual!
        while (j >= 0 and maior(lista[j], aux, k) == aux):
            lista[j+1] = lista[j]
            j -= 1
        lista[j+1] = aux # Se o loop acabar pela primeira condição, j = -1

def meu_bubble_sort(vetor):
    '''Ordena os elementos do vetor em ordem crescente.'''
    houve_troca = True
    while houve_troca:
        houve_troca = False
        for i in range(1, len(vetor)):
            if maior(vetor[i - 1], vetor[i], k) == vetor[i]:
                troca(vetor, i - 1, i)
                houve_troca = True

n, k = [int(x) for x in input().split()][:2]
numeros = []

for _ in range(n):
    numeros.append(int(input()))

insertion_sort(numeros)
printLista(numeros)
