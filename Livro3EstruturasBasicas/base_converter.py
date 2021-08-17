from DataStructuresChapter3.Stack import Stack

# Versão do divisaoPor2 generalizado para qualquer base entre 2 e 16
def baseConverter(decNumber, base):
    digits = "0123456789ABCDEF"

    remstack = Stack()

    while decNumber > 0:
        resto = decNumber % base
        remstack.push(resto)
        decNumber = decNumber // base

    newString = ""
    while not remstack.isEmpty():
        newString = newString + digits[remstack.pop()]

    return newString