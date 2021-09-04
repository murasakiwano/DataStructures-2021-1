def fatorial(N, lista):
    if N < len(lista):
        return lista[N]
    else:
        if not lista:
            lista.append(1)
        for i in range(len(lista), N+1):
            F = i*lista[i-1]
            lista.append(F)
        
    return lista[N]

def print_sequencia(L):
    strPrint = ''
    for i in range(len(L)-1):
        strPrint += str(L[i]) + ' '
    strPrint += str(L[-1])
    print(strPrint)

L = []

N = int(input())
L_TOT = []

for _ in range(N):
    x = int(input())
    F = fatorial(x, L)
    L_print = [x % 2357 for x in L[:x+1]]
    L_TOT += [L_print]

for i in range(len(L_TOT)):
    print_sequencia(L_TOT[i])
