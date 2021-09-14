def selection_sort(lista):
    for i in range(len(lista)-1):
        # Acha o menor elemento a partir da posição i
        menor = i
        for j in range(i, len(lista)):
            if lista[menor] > lista[j]:
                menor = j
        # Troca com o elemento da posição i
        lista[i], lista[menor] = lista[menor], lista[i]