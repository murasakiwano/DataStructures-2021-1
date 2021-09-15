N = int(input())

i = 0
notas = []

for _ in range(N):
    x = float(input())
    notas.append(x)

notas = sorted(notas)
pior_nota = notas[0]
mediana = notas[len(notas)//2]
melhor_nota = notas[-1]

print(f"{pior_nota:.2f}")
print(f"{mediana:.2f}")
print(f"{melhor_nota:.2f}")
