def bubble_sort(lista):
    # Valores de i em ordem decrescente
    for i in reversed(range(len(lista))):
        for j in range(i):
            # Se o elemento encontrado for maior
            # Troca com o elemento da posição i
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
