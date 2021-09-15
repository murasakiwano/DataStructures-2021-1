from collections import Counter

N = int(input())
roupas = input().split()

roupas = sorted(roupas)

repetidas = 0

# Agora que tenho as roupas ordenadas, vou verificando quantas iguais tenho
for i in range(1, len(roupas)):
    if roupas[i] == roupas[i-1]:
        repetidas += 1

print(repetidas)
