from copy import deepcopy


def average(l, att):
    soma = 0
    for team in l:
        soma += team[att]

    return soma / len(l)


times = []

dicionario = {
    'Nome': None,
    'Pontos': 0,
    'Vitórias': 0,
    'Saldo de gols': 0,
    'Gols marcados': 0,
    'Gols sofridos': 0
}

# O `-` é porque, tirando o Nome, todos ficarão em ordem decrescente
# e o nome é o único atributo que não pode receber `-`


def chave_de_ordenacao(x): return (
    -x['Pontos'],
    -x['Vitórias'],
    -x['Saldo de gols'],
    -x['Gols marcados'],
    -x['Gols sofridos'],
    x['Nome']
)


N = 20  # 20 linhas de resultado

for _ in range(N):
    d_time = deepcopy(dicionario)
    nome_resultados = input().split()
    d_time['Nome'] = nome_resultados[0]
    for partida in nome_resultados[1:]:
        P, C = int(partida[0]), int(partida[2])
        saldo = P - C
        d_time['Saldo de gols'] += saldo
        d_time['Gols marcados'] += P
        d_time['Gols sofridos'] += C
        if saldo > 0:
            d_time['Vitórias'] += 1
            d_time['Pontos'] += 3
        elif saldo == 0:
            d_time['Pontos'] += 1

    times.append(d_time)

classificacao = sorted(times, key=chave_de_ordenacao)

media_de_pontos = average(classificacao, 'Pontos')
print(f'Media de pontos: {media_de_pontos:.2f}')

liberadores = classificacao[:4]  # 4 primeiros vão pra liberadores
rebaixados = classificacao[-4:]  # 4 últimos são rebaixados pra série C

str_liberadores = ''
for champion in liberadores[:3]:
    str_liberadores += champion['Nome'] + ', '

str_liberadores += liberadores[3]['Nome']
str_liberadores = ''
for champion in liberadores[:3]:
    str_liberadores += champion['Nome'] + ', '

str_liberadores += liberadores[3]['Nome']

str_rebaixados = ''
for i in range(len(rebaixados)-1, 0, -1):
    str_rebaixados += rebaixados[i]['Nome'] + ', '

str_rebaixados += rebaixados[0]['Nome']

print(f'Liberadores: {str_liberadores}')
print(f'Rebaixados: {str_rebaixados}')
