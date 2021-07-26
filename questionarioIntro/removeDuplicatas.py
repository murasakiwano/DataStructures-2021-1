def remove_duplicatas(l):
    for i in range(len(l)):
        if i == len(l): # o loop não está evitando index out of range
            break
        elem = l[i]
        while l.count(elem) > 1:
            for j in range(i+1, len(l)):
                if j < len(l) and l[j] == elem:
                    l.pop(j)
    return l

# print(remove_duplicatas([1, 2, 3, 4, 5, 6, 2, 1, 3, 5, 1, 3, 6]))

print(remove_duplicatas([1,1,1]))
	
print(remove_duplicatas([1,2,3,4,5,6,5,4,3,2,1]))