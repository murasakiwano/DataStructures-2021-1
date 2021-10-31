from queue import Queue

# Implementar árvore de decisão que armazena os códigos


class NoArvore:
    def __init__(self, caractere='*', codigo='', esq=None, dir=None, pai=None):
        self.caractere = caractere
        self.codigo = codigo
        self.esq = esq
        self.dir = dir
        self.pai = pai

    def getChar(self):
        return self.caractere

    def getCode(self):
        return self.codigo

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def insereEsq(self, no):
        self.esq = no
        self.esq.pai = self

    def insereDir(self, no):
        self.dir = no
        self.dir.pai = self

    def filhoEsq(self):
        return self.esq

    def filhoDir(self):
        return self.dir

    def ehEsq(self):
        return (self.pai and self.pai.esq == self)

    def ehDir(self):
        return (self.pai and self.pai.dir == self)

    def ehRaiz(self):
        return not self.pai

    def ehFolha(self):
        return not (self.esq or self.dir)

    def temFilho(self):
        return self.esq or self.dir

    def tem2Filhos(self):
        return self.esq and self.dir

    def substituiDados(self, caractere, codigo, esq=None, dir=None):
        self.caractere = caractere
        self.codigo = codigo
        if esq == None:
            esq = self.esq
        if dir == None:
            dir = self.dir
        self.esq = esq
        self.dir = dir


class ArvoreDeDecisao:
    def __init__(self):
        self.raiz = None
        self.tam = 0

    def __len__(self):
        return self.tam

    def setRaiz(self, raiz: NoArvore):
        self.raiz = raiz

    def insereNo(self, no: NoArvore):
        # função que recebe um no e o coloca na árvore
        # tem que ser de acordo com o pedido
        # esquerda para representar ponto ('.') e
        # direita para representar traço ('-')
        # Preciso colocar e alocar de acordo com o dito acima
        # É fazer o nó ir descendo de acordo com *código*
        # Se não tiver um filho, cria um nó vazio
        caractere = no.caractere
        codigo = no.codigo

        if not self.raiz:
            self.raiz = NoArvore()

        noAtual = self.raiz

        while codigo != '':

            if codigo[0] == '.':
                if not noAtual.esq:
                    noEsq = NoArvore()
                    noAtual.insereEsq(noEsq)
                noAtual = noAtual.esq
                codigo = codigo[1:]

            elif codigo[0] == '-':
                if not noAtual.dir:
                    noDir = NoArvore()
                    noAtual.insereDir(noDir)
                noAtual = noAtual.dir
                codigo = codigo[1:]

        noAtual.substituiDados(no.caractere, no.codigo)

    def __str__(self):
        # * fazer uma level-order traversal da árvore
        strp = ''

        if self.raiz is None:
            return strp

        q1 = Queue()
        q2 = Queue()
        q1.put(self.raiz)

        while (not q1.empty()) or (not q2.empty()):
            while not q1.empty():
                noAtual = q1.get()
                strp += str(noAtual.getChar()) + ' '
                if noAtual.filhoEsq() is not None:
                    q2.put(noAtual.filhoEsq())
                if noAtual.filhoDir() is not None:
                    q2.put(noAtual.filhoDir())

            while not q2.empty():
                noAtual = q2.get()
                strp += str(noAtual.getChar()) + ' '
                if noAtual.filhoEsq() is not None:
                    q1.put(noAtual.filhoEsq())
                if noAtual.filhoDir() is not None:
                    q1.put(noAtual.filhoDir())

        return strp

    def traverse_by_code(self, codigo: str) -> str:
        if self.raiz is None:
            return 'ERROR'

        noAtual = self.raiz

        symbol = ''

        while codigo != '':
            if codigo[0] == '.':
                if noAtual.filhoEsq() is not None:
                    noAtual = noAtual.filhoEsq()
                else:
                    return 'ERROR'
                codigo = codigo[1:]
            elif codigo[0] == '-':
                if noAtual.filhoDir() is not None:
                    noAtual = noAtual.filhoDir()
                else:
                    return 'ERROR'
                codigo = codigo[1:]
            elif codigo[0] == '/':
                symbol += ' '
                codigo = codigo[1:]

        symbol += str(noAtual.getChar())

        return symbol

    def traverse_by_char(self, caractere: str):
        if self.raiz is None:
            return 'ERROR'
        symbol = ''

        q1 = Queue()
        q2 = Queue()
        q1.put(self.raiz)

        found = False

        while (not q1.empty()) or (not q2.empty()) and not found:
            while not q1.empty():
                noAtual = q1.get()
                if noAtual.getChar() == caractere:
                    symbol = noAtual.getCode()
                    found = True
                if noAtual.filhoEsq() is not None:
                    q2.put(noAtual.filhoEsq())
                if noAtual.filhoDir() is not None:
                    q2.put(noAtual.filhoDir())

            while not q2.empty():
                noAtual = q2.get()
                if noAtual.getChar() == caractere:
                    symbol = noAtual.getCode()
                    found = True
                if noAtual.filhoEsq() is not None:
                    q1.put(noAtual.filhoEsq())
                if noAtual.filhoDir() is not None:
                    q1.put(noAtual.filhoDir())

        if not found:
            return 'ERROR'

        return symbol


def codificar(tree: ArvoreDeDecisao, msg: str):
    coded = ''

    ultimoFoiEspaco = False

    for char in msg:
        if char == ' ' and not ultimoFoiEspaco:
            coded += '/'
            ultimoFoiEspaco = True
        elif char != ' ':
            ultimoFoiEspaco = False
            codedSym = tree.traverse_by_char(char)
            if codedSym == 'ERROR':
                return 'Impossível codificar a mensagem!'
            coded += codedSym + ' '

    return coded


def decodificar(tree: ArvoreDeDecisao, msg: str):
    decoded = ''
    msg = msg.split()

    for codigo in msg:
        decSym = tree.traverse_by_code(codigo)
        if decSym == 'ERROR':
            return 'ERROR'
        decoded += decSym

    return decoded


arvore = ArvoreDeDecisao()

no1 = NoArvore()
arvore.setRaiz(no1)

N = int(input())

for _ in range(N):
    CHAR, CODE = input().split()
    node = NoArvore(caractere=CHAR, codigo=CODE)
    arvore.insereNo(node)

COMANDO = int(input())

MSG = input()

if COMANDO == 0:
    RES_MSG = decodificar(arvore, MSG)
elif COMANDO == 1:
    RES_MSG = codificar(arvore, MSG)

print(RES_MSG)

if RES_MSG != 'Impossível codificar a mensagem!':
    print(arvore)

