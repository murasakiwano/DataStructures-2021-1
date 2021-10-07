class BinHeap:
    def __init__(self):
        self.heapList = [0] # this is to make the list start nonempty
        self.currentSize = 0

    def isEmpty(self):
        return self.heapList == [0]

    def size(self):
        return self.currentSize

    # percUp percolates a new item as far up in the tree as it needs
    # to go to maintain the heap property
    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2
    
    # adds a new item to the heap
    def insert(self, k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    # percDown percolates a new item as far down in the tree as it needs
    # to go to maintain the heap property
    def percDown(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc
    
    # return the key value of the minimum child of a node
    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2] <  self.heapList[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    # returns the item with the minimum key value, leaving the item
    # in the heap
    def findMin(self):
        return self.heapList[1]
    
    # returns the item with the minimum key value, removing the item
    # from the heap
    def delMin(self):
        retVal = self.heapList[self.currentSize]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retVal

    # builds a heap from a list of keys
    def buildHeap(self, alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.percDown(i)
            i -= 1

bh = BinHeap()
bh.buildHeap([9,5,6,2,3])

print(bh.heapList)
print(bh.findMin())
print(bh.size())
bh.insert(-1)
print(bh.heapList)
