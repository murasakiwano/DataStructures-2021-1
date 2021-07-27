# Os critérios para uma string ser palíndromo são diferentes a depender da 
# paridade do seu comprimento.
# Se a string tiver comprimento par, a gente precisa que cada caractere tenha
# um simétrico igual. Caso seja ímpar, o caractere do meio pode ser qualquer um.
# Como o índice começa do 0, o caractere do meio se dá por len(s) // 2.
# OBS: Simétrico de s[0] == s[-1], s[1] == s[-2], etc.
def palindrome(s):
    count = 0 # Se count > 1 ao final do loop, impossível
    if len(s) % 2 == 0:
        for i in range(len(s)//2):
            if s[i] != s[-i - 1]:
                count += 1
    else:
        for i in range(len(s) // 2 ):
            if s[i] != s[-i - 1]:
                count += 1
    
    # Se a string tiver comprimento ímpar você pode trocar o do meio
    if count == 1 or (count == 0 and len(s) % 2 != 0):
        return "POSSÍVEL"
    else:
        return "IMPOSSÍVEL"


s = input()

print(palindrome(s))