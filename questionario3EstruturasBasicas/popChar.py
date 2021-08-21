class Stack: # considerando que o topo é o fim da lista
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)
        # se o topo fosse o começo da lista:
        # self.items.insert(0, item)

    def pop(self):
        return self.items.pop()
        # se o topo fosse o começo da lista:
        # self.items.pop(0)

    def peek(self):
        return self.items[-1]
        # se o topo fosse o começo da lista:
        # self.items[0]

    def size(self):
        return len(self.items)   

s = input()
f = Stack()
sNew = ''

for i in range(len(s)):
    if s[i] == '*':
        temp = f.pop()
        if temp:
            sNew = sNew + temp
    else:
        f.push(s[i])

print(sNew)