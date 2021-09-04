# Escrever uma função que implementa fibonacci e o número de chamadas
# Tem de ser a versão **recursiva** tradicional de fibonacci

contador = 0

def Fib(n):
    global contador
    contador += 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fib(n-2) + Fib(n-1)

n = int(input())

f = Fib(n)
print(f"Fib({n}) = {f} ({contador} chamadas)")