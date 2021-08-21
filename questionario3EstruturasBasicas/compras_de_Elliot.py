# As compras de Elliot
class Node:
    def __init__(self, initData):
        self.data = initData
        self.next = None

    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next
    
    def setData(self, newData):
        self.data = newData
    
    def setNext(self, newNext):
        self.next = newNext

class OrderedList:
    def __init__(self):
        self.head = None
    
    # Os métodos isEmpty, length e remove são os mesmos da lista não-ordenada
    def isEmpty(self):
        return self.head == None # Se não aponta para a cabeça, tá vazia

    def length(self):
        current = self.head
        count = 0
        while current:
            count = count + 1
            current = current.getNext()
        
        return count

    def remove(self, item):
        previous = None
        current = self.head
        found = False
        while current and not found:
            if current.getData()[0] == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    # Para o search, nós usamos o fato de que a lista está ordenada
    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current == current.getNext()

        return found
    
    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData()[1] < item[1]:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def index(self, item):
        current = self.head
        count = 0
        while current.getData() != item:
            count = count + 1
            current = current.getNext()
        
        return count

    def pop(self, pos=-1):
        if pos == -1:
            pos = self.length() - 1

        current = self.head
        previous = None
        for _ in range(pos):
            previous = current
            current = current.getNext()

        item = current.getData()
        previous.setNext(current.getNext())

        return item

s = input()

shopping_list = OrderedList()

while s != "fim":
    s = s.split()
    if s[0] == '-':
        shopping_list.remove(s[1])
    else:
        s[1] = float(s[1])
        shopping_list.add((s[0], s[1]))
    
    s = input()

def print_list(l):
    current = l.head
    num_items = l.length()
    preco_total = 0
    while current:
        nome, preco = current.getData()
        preco_total = preco_total + preco
        print(f'{nome}: R$ {preco:.2f}')
        current = current.getNext()

    print("----------------------")
    print(f'{num_items} item(ns): R$ {preco_total:.2f}')

print_list(shopping_list)