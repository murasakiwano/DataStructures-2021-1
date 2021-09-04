# Aqui, a ideia é utilizar uma função recursiva para gerar todas as combinações
# possíveis da lista.
# A ideia é gerar as combinações de tal forma:
#   - Colocar o último elemento da sublista, um por vez

def gerar_combinacoes(L):
    if L == []:
        return [L]
    else:
        head = gerar_combinacoes(L[:-1])
        return head + [c + [L[-1]] for c in head]

def eh_possivel_ganhar(combinacoes: list, sorteado: int) -> bool:
    for c in combinacoes:
        if sum(c) == sorteado:
            return True
    
    return False

premios = [int(x) for x in input().split()]
numero_sorteado = int(input())

combinacoes = gerar_combinacoes(premios)

if eh_possivel_ganhar(combinacoes, numero_sorteado):
    print("E possivel ganhar.")
else:
    print("Impossivel ganhar.")