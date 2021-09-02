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

print(fibonacci(10))