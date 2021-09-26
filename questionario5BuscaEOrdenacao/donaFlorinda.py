def crescente(a, b):
    '''Retorna True se a <= b, False caso contrário.'''
    return (maior(a, b) == b)


def troca(vetor, a, b):
    '''Troca os conteúdos dos inteiros.'''
    vetor[a], vetor[b] = vetor[b], vetor[a]


def merge(esquerda, direita):
    vetor = []

    while esquerda and direita:
        if crescente(esquerda[0], direita[0]):
            vetor.append(esquerda.pop(0))
        else:
            vetor.append(direita.pop(0))

    if esquerda:
        vetor.extend(esquerda)
    if direita:
        vetor.extend(direita)

    return vetor


def merge_sort(vetor):
    '''Ordena os elementos do vetor em ordem crescente.'''
    if len(vetor) < 2:
        return vetor

    meio = len(vetor) // 2
    esquerda = merge_sort(vetor[:meio])
    direita = merge_sort(vetor[meio:])
    return merge(esquerda, direita)


def transforma_em_heap(vetor, inicial, final):
    esquerda = 2 * inicial + 1
    direita = esquerda + 1

    max = inicial
    if esquerda <= final and not crescente(vetor[esquerda], vetor[inicial]):
        max = esquerda
    if(direita <= final and not crescente(vetor[direita], vetor[max])):
        max = direita

    if max != inicial:
        troca(vetor, inicial, max)
        transforma_em_heap(vetor, max, final)


def heap_sort(vetor):
    '''Ordena os elementos do vetor em ordem crescente.'''
    for i in range(len(vetor) // 2, -1, -1):
        transforma_em_heap(vetor, i, len(vetor) - 1)

    for i in range(len(vetor) - 1, 0, -1):
        troca(vetor, 0, i)
        transforma_em_heap(vetor, 0, i - 1)


N = int(input())
pretendentes = []


def maior(p1, p2):
    # return sorted([p1, p2], key=lambda x: x['nome'])[-1]
    if p1['altura'] != p2['altura'] and abs(p1['altura']-180) != abs(p2['altura']-180):
        return sorted([p1, p2], key=lambda x: abs(x['altura']-180))[0]
    else:
        if p1['peso'] == p2['peso']:
            if p1['sobrenome'] != p2['sobrenome']:
                return sorted([p1, p2], key=lambda x: x['sobrenome'])[0]
            else:
                return sorted([p1, p2], key=lambda x: x['nome'])[0]
        else:
            if p1['peso'] > 75 and p2['peso'] < 75:
                return p2
            elif p2['peso'] > 75 and p1['peso'] < 75:
                return p1
            else:
                return sorted([p1, p2], key=lambda x: abs(x['peso']-75))[0]


for _ in range(N):
    pret = input().split()
    temp = {}
    temp['nome'] = pret[0]
    temp['sobrenome'] = pret[1]
    temp['peso'] = int(pret[3])
    temp['altura'] = int(pret[2])
    pretendentes.append(temp)

heap_sort(pretendentes)

pretendentes.reverse()

for p in pretendentes:
    print(f"{p['sobrenome']}, {p['nome']}")
