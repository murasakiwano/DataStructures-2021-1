from timeit import Timer

def len01(palavra):
    resposta = 0
    for _ in palavra:
        resposta += 1
    return resposta

def len02(palavra):
    return len(palavra) 

tempos01 = []
tempos02 = []

intervaloDeTestes = range(10000, 100000, 10000)
for tamanhoDoTeste in intervaloDeTestes:
    palavraDeTeste = 'a' * tamanhoDoTeste
    f01 = f'len01("{palavraDeTeste}")'
    f02 = f'len02("{palavraDeTeste}")'
    timer01 = Timer(f01, "from __main__ import len01")
    timer02 = Timer(f02, "from __main__ import len02")
    tempos01.append(timer01.timeit(number = 1000))
    tempos02.append(timer02.timeit(number = 1000))

print(tempos01)
print(tempos02)