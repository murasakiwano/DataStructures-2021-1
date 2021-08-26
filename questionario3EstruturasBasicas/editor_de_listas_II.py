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
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def append(self, item):
        previous = None
        current = self.head
        newItem = Node(item)
        l = self.length()

        if self.head == None:
            self.head = newItem

        for _ in range(l):
            previous = current
            current = current.getNext()
        
        if previous:
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

    def pop(self, pos=-1):
        if pos == -1:
            pos = self.length() - 1

        current = self.head
        previous = None
        for _ in range(pos):
            previous = current
            current = current.getNext()

        item = current.getData()
        if previous:
            previous.setNext(current.getNext())
        else:
            self.head = current.getNext()

        return item
    
    def printLista(self):
        current = self.head
        for _ in range(self.length()):
            print(current.getData())
            current = current.getNext()

stop = False
lista = UnorderedList()

# lista.add(2)
# lista.add(3)
# i = lista.index(3)
# lista.remove(3)
# lista.insert(i, 4)

while True:
    s = input().split()
    if s[0] == 'F':
        lista.append(int(s[1]))
    elif s[0] == 'I':
        lista.add(int(s[1]))
    elif s[0] == 'E':
        item = lista.pop(int(s[1]) - 1)
        print(item)
    elif s[0] == 'T':
        item = int(s[1])
        i = lista.index(item)
        t = lista.remove(item)
        n = int(s[2])
        lista.insert(i, n)
    elif s[0] == 'P':
        item = lista.pop()
        print(item)
    elif s[0] == 'D':
        item = lista.pop(0)
        print(item)
    elif s[0] == 'X':
        print()
        lista.printLista()
        break