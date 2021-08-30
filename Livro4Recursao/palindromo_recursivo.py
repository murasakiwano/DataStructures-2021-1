# Função que remove espaço em branco e pontuação
# Também deixa em minúscula. Basicamente "normaliza" uma string
def removeWhite(s):
    if s:
        if len(s) == 1:
            if str.isalpha(s[0]):
                return s[0].lower()
            else:
                return ""
        else:
            if str.isalpha(s[0]):
                return removeWhite(s[1:]) + s[0].lower()
            else:
                return removeWhite(s[1:])
    return ""

def isPal(s):
    if s:
        if len(s) == 1:
            return True
        else: 
            if s[0] == s[-1]:
                return isPal(s[1:])
    return True

print(isPal(removeWhite("Go hang a salami; I’m a lasagna hog.")))
print(isPal(removeWhite("Reviled did I live, said I, as evil I did deliver")))
print(isPal(removeWhite("Wassamassaw")))
print(isPal(removeWhite("Able was I ere I saw Elba")))
