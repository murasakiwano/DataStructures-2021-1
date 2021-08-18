from Node import Node

class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None # Se não aponta para a cabeça, tá vazia
    
    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def length(self):
        current = self.head
        count = 0
        while current:
            count = count + 1
            current = current.getNext()
        
        return count

    def search(self, item):
        current = self.head
        found = False
        while current and not found:
            if current.data == item:
                found = True
            else:
                current = current.getNext()

        return found

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

    def append(self, item):
        previous = None
        current = self.head
        newItem = Node(item)
        l = self.length()

        for i in range(l):
            previous = current
            current.setNext(current.getNext)
        
        previous.setNext(newItem)

    def insert(self, pos, item):
        previous = None
        current = self.head
        count = 0
        newItem = Node(item)

        if pos == 0:
            newItem.setNext(self.head)
            self.head = newItem
        else:
            while count < pos:
                count = count + 1
                previous = current
                current = current.getNext()
            
            previous.setNext(newItem)
            newItem.setNext(current)

    def index(self, item):
        current = self.head
        count = 0
        while current.data != item:
            count = count + 1
            current = current.getNext()
        
        return count

    def pop(self):
        l = self.length()
        current = self.head
        previous = None
        for i in range(l-1):
            previous = current
            current = current.getNext()
        
        item = current.getData()
        previous.setNext(None)

        return item