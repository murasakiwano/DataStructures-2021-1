from Pilha import Pilha

def divisaoPor2(decNumber):
    restoPilha = Pilha()

    while decNumber > 0:
        resto = decNumber % 2
        restoPilha.push(resto)
        decNumber = decNumber // 2

    binString = ""
    while not restoPilha.isEmpty():
        binString = binString + str(restoPilha.pop())

    return binString