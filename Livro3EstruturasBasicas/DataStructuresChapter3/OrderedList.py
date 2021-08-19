from Node import Node

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
            if current.getData() == item:
                found = True
            else:
                previous = current
                current.setNext(current.getNext())

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
            if current.getData() > item:
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