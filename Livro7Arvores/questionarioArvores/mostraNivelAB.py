def mostra_nivel(raiz, nivel, atual=0):
    if raiz is None:
        return
    if atual == nivel:
        mostra(raiz)
        return

    mostra_nivel(raiz.esq, nivel, atual+1)
    mostra_nivel(raiz.dir, nivel, atual+1)

# Programa que mostra uma árvore binária por parênteses aninhados
def mostra_aux(raiz, repStr=['(']):
    # caso base
    if not raiz:
        return
    # elif not (raiz.esq or raiz.dir):
        
    repStr.append(str(raiz.dado))

    # se é nó folha, retorna
    if not raiz.esq and not raiz.dir:
        repStr.append(' () ()')
        return
    
    # subárvore da esquerda
    repStr.append(' (')
    mostra_aux(raiz.esq, repStr)
    repStr.append(')')

    # subárvore da direita
    repStr.append(' (')
    if not raiz.dir:
        repStr.append('')
    else:
        mostra_aux(raiz.dir, repStr)
    repStr.append(')')

    return

def mostra(raiz):
    repStr = ['(']
    mostra_aux(raiz, repStr)
    repStr += [')']
    print(''.join(repStr))

class Node:
    def __init__(self, dado):
        self.dado = dado
        self.esq = None
        self.dir = None

if __name__=='__main__':
    #       1
    #     /   \
    #    2     3
    #           \
    #            4
 
    root = Node(1)
    root.esq = Node(2)
    root.dir = Node(3)
    root.dir.dir = Node(4)
    mostra_nivel(root, 2)
