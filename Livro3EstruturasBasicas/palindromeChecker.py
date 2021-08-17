from DataStructuresChapter3.Deque import Deque

def palindChecker(aString):
    charDeque = Deque()

    for c in aString:
        charDeque.addRear(c)

    while charDeque.size() >= 2:
        a = charDeque.removeFront()
        b = charDeque.removeRear()
        
        if a != b:
            return False
    
    return True

print(palindChecker("lsdkjfskf"))
print(palindChecker("radar"))