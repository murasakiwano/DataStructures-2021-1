# Escrever uma função que implementa fibonacci e o número de chamadas
# Tem de ser a versão **recursiva** tradicional de fibonacci

contador = 0

def Fib(n, cont):
    global contador
    contador += 1
    if n == 0:
        return 0, cont
    elif n == 1:
        return 1, cont
    else:
        return Fib(n-2, cont + 1)[0] + Fib(n-1, cont + 1)[0], cont

n = int(input())

f, c = Fib(n, 0)
print(f"Fib({n}) = {f} ({c} chamadas)")