def shell_short(lista):
    h = len(lista) // 2
    while h > 0:

        for inicio in range(h):
            gapInsertionSort(lista, inicio, h)

        h = h // 2


def gapInsertionSort(lista, inicio, gap):
    for i in range(inicio+gap, len(lista), gap):
        current = lista[i]
        pos = i

        while pos >= gap and lista[pos-gap] > current:
            lista[pos] = lista[pos-gap]
            pos -= gap

        lista[pos] = current
