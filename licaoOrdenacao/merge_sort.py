def merge (v, inicio, meio, fim, aux):
    # indices da metade inf, sup e aux respc.
    i = inicio; j = meio+1; k = 0;
    # enquanto não avaliou completamente um dos
    # vetores, copia menor elemento para aux
    while (i <= meio and j <= fim):
        if (v[i] <= v[j]):
            aux[k] = v[i]
            k = k + 1
            i = i + 1
        else:
            aux[k] = v[j]
            k = k + 1
            j = j + 1 
    #copia resto da primeira sub-lista
    while (i <= meio):
        aux[k] = v[i]
        k = k + 1
        i = i + 1
    # copia resto da segunda sub-lista
    while (j <= fim):
        aux[k] = v[j]
        k = k + 1
        j = j + 1
    i = inicio; k = 0;
    # copia lista ordenada aux para v
    while (i <= fim):
        v[i] = aux[k]
        i = i + 1
        k = k + 1

def merge_sort(v, inicio, fim, aux):
    meio = (fim + inicio) // 2
    if (inicio < fim):
        merge_sort(v, inicio, meio, aux)
        merge_sort(v, meio+1, fim, aux)
        merge(v, inicio, meio, fim, aux)