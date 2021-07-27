def sum(l):
    soma = 0
    for x in l:
        soma += x
    return soma

n = int(input())

if n < 12 or n > 10**2:
    raise ValueError("Só pode ter entre 12 e 100 jogadores no plantel!")

a = [int(x) for x in input().split()]

if len(a) != n:
    raise ValueError("Quantidade de jogadores diferente da mencionada!")

# Dado que temos 11 + x jogadores, basta pegar os x jogadores com menor 
# habilidade e colocar no time reserva, sendo que x não pode superar 11.
a.sort()

if len(a) <= 22:
    x = len(a) - 11
    reserva = a[:x]
    titular = a[x:]
else:
    r = len(a) - 22
    x = len(a) - 11
    naoRelacionado = a[:r]
    reserva = a[r:x]
    titular = a[x:]

habilidadesTitular = sum(titular)
habilidadesReserva = sum(reserva)

print(habilidadesTitular - habilidadesReserva)