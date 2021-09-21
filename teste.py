import sys

N = int(input())
for i in range(N):
    sys.system(f'python3 solucao.py < entrada{i}.txt')
    sys.system(f'diff saida{i}.txt gabarito{i}.txt')