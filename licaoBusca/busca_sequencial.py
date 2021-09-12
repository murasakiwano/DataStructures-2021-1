def busca_sequencial(lista, item):
    for e in lista:
        if e == item:
            return True

    return False

def busca_sequencial_elegante(lista, item):
    if lista[0] == item:
        return True
    return False or busca_sequencial_elegante(lista[1:], item)