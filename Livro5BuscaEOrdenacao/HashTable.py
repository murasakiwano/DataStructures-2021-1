class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hashValue = self.hashfunction(key, len(self.slots))
        startSlot = hashValue

        if self.slots[hashValue] == None:
            self.slots[hashValue] = key
            self.data[hashValue] = data
        else:
            if self.slots[hashValue] == key:
                self.data[hashValue] == data  # replace
            else:
                nextSlot = self.rehash(hashValue, len(self.slots))
                while self.slots[nextSlot] != None and \
                        self.slots[nextSlot] != key and \
                        nextSlot != startSlot:
                    nextSlot = self.rehash(nextSlot, len(self.slots))

                    if self.slots[nextSlot] == None:
                        self.slots[nextSlot] = key
                        self.data[nextSlot] = data
                    else:
                        self.data[nextSlot] = data  # replace

    def hashfunction(self, key, size):
        return key % size

    def rehash(self, oldhash, size):
        return (oldhash+1) % size

    def get(self, key):
        startSlot = self.hashfunction(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = startSlot
        while self.slots[position] != None and \
                not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == startSlot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

    def len(self):
        return len(self.slots)

    def __contains__(self, key):
        return (key in self.slots)

    def __delitem__(self, key):
        pos = self.slots.index(key)
        del self.data[pos]
        del self.slots[pos]

d = HashTable()
d.put(10, 1)
del d[10]
print(10 in d)