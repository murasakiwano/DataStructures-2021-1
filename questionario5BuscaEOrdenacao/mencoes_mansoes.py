dict_mencoes = {'SR': 0,
                'II': 1,
                'MI': 2,
                'MM': 3,
                'MS': 4,
                'SS': 5}

N = int(input())
lista = []

for _ in range(N):
    s = input().split()
    lista += [(s[0], ' '.join(s[1:]))]

lista = sorted(lista, key = lambda x: (-dict_mencoes[x[0]], x[1]))
for aluno in lista:
    print(aluno[0], aluno[1])