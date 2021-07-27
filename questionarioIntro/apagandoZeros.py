# Basta checar: se o caractere i for 1 e o seguinte for zero, soma o contador 
# até que seja 1. E faz assim até terminar a string. O valor do contador é o
# número mínimo de zeros para apagar.

def apagarZeros(s):
    count = 0
    jaFoiUm = False
    for i in range(len(s)):
        if s[i] == '1':
            jaFoiUm = True
        elif jaFoiUm and (s[i] == '0' and '1' in s[i:]):
            count += 1
    return count

n = int(input())
for i in range(n):
    s = input()
    print(apagarZeros(s))