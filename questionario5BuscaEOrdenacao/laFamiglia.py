p = int(input())
c = [int(x) for x in input().split()][:p]

d = []

for casa in c:
    soma = 0
    for j in range(len(c)):
        if casa != c[j]:
            soma += abs(casa - c[j])
    
    d.append(soma)

d = sorted(d, key=lambda x: x)

print(d[0])
