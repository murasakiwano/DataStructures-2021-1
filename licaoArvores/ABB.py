# Árvore Binária ou Árvore Binária de Busca
class No_ABB():
    def __init__(self, dado, esquerda=None, direita=None):
        self.dado = dado
        self.esquerda = esquerda
        self.direita = direita

class No_ABB2():
    def __init__(self, dado, pai=None, esquerda=None, direita=None):
        self.dado = dado 
        self.esquerda = esquerda
        self.direita = direita
        self.pai = pai


