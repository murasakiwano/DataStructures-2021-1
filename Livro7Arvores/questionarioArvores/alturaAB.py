# Questão 1: Altura da Árvore Binária
# altura = tamanho do caminho mais longo da raiz até uma de suas folhas
def altura(raiz):
    # Caso base: nó folha
    if not raiz or not (raiz.dir or raiz.esq):
        return 0

    else:
        # Calcular a altura da subárvore esquerda e direita
        alturaEsq = altura(raiz.esq)
        alturaDir = altura(raiz.dir)

        # Usar a com maior altura
        if (alturaDir > alturaEsq):
            return alturaDir + 1
        else:
            return alturaEsq + 1
