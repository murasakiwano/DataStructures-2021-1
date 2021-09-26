from collections import Counter
n = int(input())
l = []

def str2list(s):
    m = []
    m[:0] = s
    return m

def removeDuplicatas(st):
    s = set()

    for i in st:
        s.add(i)
    
    st = ""
    for i in s:
        st += i
    return st

for _ in range(n):
    # Cada caso de teste contém 4 linhas
    joga = False
    i = 0
    conteudos = Counter(str2list(input()))
    matutino =  str2list(input())
    vespertino =  str2list(input())
    noturno =  str2list(input())
    turnos = [matutino, vespertino, noturno]
    joga = False
    for i in range(3):
        if joga:
            break
        for c in turnos[i]:
            if c in conteudos.keys():
                conteudos[c] -= 1
                if conteudos[c] <= 0:
                    del conteudos[c]
            else:
                if turnos[i] != []:
                    print("You died!")
                    joga = True
                    break

    if not joga:
        if not conteudos:
            print("It's in the box!")
        else:
            conteudo = sorted(list(conteudos.keys()))
            conteudos = ''.join(conteudo)
            print(f"Bora ralar: {conteudos}")
