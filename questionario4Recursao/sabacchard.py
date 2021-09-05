combinacoes = []

def gerar_combinacoes(cartas, combinacoes): # Função que vai gerar as combinações possíveis
    if cartas == []:
        return [cartas]
    else:
            head = gerar_combinacoes(cartas[:-1])
            return head + [carta + [cartas[-1]] for carta in head]

N = int(input())           
L = [int(x) for x in input().split()]
gerar_combinacoes(L)
combs = list(filter(lambda x: len(x) == N / 2, combinacoes))
sum_combs = [sum(x) for x in combs]
largest_sum = max(sum_combs)
print(largest_sum)