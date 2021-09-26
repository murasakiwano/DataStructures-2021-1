a, t = tuple(int(x) for x in input().split())[:2]
alunos = []

for _ in range(a):
    aluno = input().split()
    ira = float(aluno[0])
    nome = ' '.join(aluno[1:])
    alunos.append((ira, nome))

alunos = sorted(alunos, key=lambda aluno: (aluno[0], aluno[1]), reverse=True)

for _ in range(t):
    i = int(input())
    print(f"{alunos[i-1][1]} ({alunos[i-1][0]:.2f})")
