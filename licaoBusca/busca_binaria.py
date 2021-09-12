def busca_binaria(lista, item):
    if not lista:
        return False
    
    meio = len(lista) // 2
    if lista[meio] == item:
        return True
    elif lista[meio] < item:
        # vamos examinar o segmento direito da lista
        return busca_binaria(lista[meio+1:], item)
    else:
        # vamos examinar o segmento esquerdo da lista
        return busca_binaria(lista[:meio], item)