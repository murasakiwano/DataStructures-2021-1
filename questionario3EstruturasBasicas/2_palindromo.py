class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()
    
    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

def ehPalindromo(s):
    charDeque = Deque()

    for c in s:
        charDeque.addRear(c)

    while charDeque.size() >= 2:
        a = charDeque.removeFront()
        b = charDeque.removeRear()

        if a != b:
            return False
    
    return True

LS = input().split()
L_Janelas = []

# Usar uma janela deslizante para gerar todas as combinações
# de substrings candidatas
for palavra in LS:
    dequePalavra = Deque()
    if ehPalindromo(palavra):
        continue
    for k in range(3, len(palavra)+1):
        i=0
        while (i+k) <= len(palavra):
            dequePalavra.addRear(palavra[i:i+k])
            i += 1
        
    L_Janelas.append(dequePalavra.items)

# Aqui, tenho uma lista que contém listas com as janelas de cada palavra
L_final = []
for lista in L_Janelas:
    l = lista[1:]
    palindromos = []
    palindromos.append(lista[0])
    for p in l:
        if ehPalindromo(p):
            if p not in palindromos:
                palindromos.append(p)
    L_final.append(palindromos)

# Agora, L_final possui a palavra e seus palíndromos
# Vou percorrer de trás para frente a lista
# Se uma palavra está dentro de alguma outra palavra, ela não conta
lista_2palind = []
for lista in L_final:
    conta_2palind = 1
    l = lista[1:]
    for i in range(len(l)-1,0,-1):
        if l[i] not in l[:i]:
            conta_2palind += 1
            if conta_2palind == 2:
                lista_2palind.append(lista[0])
                continue
        
for palind2 in lista_2palind:
    print(palind2)
