def binarySearch(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist) // 2
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:
                return binarySearch(alist[:midpoint], item)
            else:
                return binarySearch(alist[midpoint+1:], item)


def binarySearch2(alist, item, first, last):
    if last >= first:
        midpoint = (first+last) // 2

        if alist[midpoint] == item:
            return True

        else:
            if item < alist[midpoint]:
                return binarySearch2(alist, item, first, midpoint-1)
            else:
                return binarySearch2(alist, item, midpoint+1, last)
    else:
        return False


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42, ]
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 13))
print(binarySearch2(testlist, 3, 0, len(testlist)-1))
print(binarySearch2(testlist, 13, 0, len(testlist)-1))
