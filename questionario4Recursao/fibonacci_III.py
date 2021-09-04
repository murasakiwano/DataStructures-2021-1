
dicionario = {}

def fibonacci_III(n):

    if n not in dicionario.keys():
        dicionario[n] = 1
    else:
        dicionario[n] += 1

    if n <= 1:
        return n
    else:
        return fibonacci_III(n-1) + fibonacci_III(n-2)

N = int(input())

F = fibonacci_III(N)

print(f"fibonacci({N}) = {F}.")

L = list(dicionario.keys())
L.reverse()

for x in L:
    print(f"{dicionario[x]} chamada(s) a fibonacci({x}).")