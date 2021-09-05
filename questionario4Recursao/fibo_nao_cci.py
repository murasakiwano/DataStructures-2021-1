# Função para imprimir os valores como pedido
def print_sequencia(L):
    strPrint = ''
    for i in range(len(L)-1):
        strPrint += str(L[i]) + ', '
    strPrint += str(L[-1])
    print(strPrint)

# Função que calcula os n primeiros números de fibonacci 
# e retorna a lista com eles
def fibonacci(n):
    if n == 0:
        return []
    if n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib1 = fibonacci(n-1)
        return fib1 + [fib1[-1] + fib1[-2]]

def gen_fibonacci(n):
    
    while True:
        n += 1
        F = fibonacci(n)
        yield F[-2], F[-1]

N = int(input())
i = 4
count = 0
L = []
gen = gen_fibonacci(i)

while count != N:
    G = next(gen)
    if G[1] - G[0] > 1:
        for j in range(G[0]+1, G[1]):
            L.append(j)
            count += 1
            if count == N:
                break

print_sequencia(L)