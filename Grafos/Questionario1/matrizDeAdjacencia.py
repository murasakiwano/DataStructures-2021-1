# Questão 1 - Matriz de Adjacência
V, E, T = input().split()
V = int(V)
E = int(E)

# Inicializar matriz
matriz = [[0 for _ in range(V)] for _ in range(V)]
i = 0

while i < E:
    X, Y, P = [int(x) for x in input().split()]
    matriz[X-1][Y-1] = P
    if T == 'N':
        matriz[Y-1][X-1] = P
    i += 1

for row in matriz:
    print(f"{row[0]:4d}", end="")
    for el in row[1:-1]:
        print(f"{el:4d}", end="")
    print(f"{row[-1]:4d}")
