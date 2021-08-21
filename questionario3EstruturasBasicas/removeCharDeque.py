# Remoção de Caracteres com Deque
# Classe para o Deque
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
    
    def getItems(self):
        return self.items

s = input() # String recebida

d = Deque()

sNew = ''

for i in range(len(s)):
    if s[i] == '*':
        temp = d.removeFront()
        if temp:
            sNew = sNew + temp
    elif s[i] == '+':
        temp = d.removeRear()
        if temp:
            sNew = sNew + temp
    elif s[i].isdigit():
        d.addRear(s[i])
    else:
        d.addFront(s[i])

print(sNew)