# Preciso fazer somente uma função que calcula a soma de uma lista recursivamente
# Depois, usar a lista como entrada para a função

def soma(L):
    if len(L) == 1:
        print(L[0])
        return L[0]
    print(f"{L[0]} + soma({L[1:]})")
    return L[0] + soma(L[1:])

n = int(input())
L = [2*x - 1 for x in range(1, n+1)]

quadrado = soma(L)

print("---------------")
print(f"{n} ** 2 == {quadrado}")