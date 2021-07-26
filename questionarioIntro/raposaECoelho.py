from math import sqrt

# O coelho leva t segundos para chegar a um buraco. Já a raposa leva
# t/2 segundos para chegar a um buraco na mesma distância.
# Logo, para que um coelho consiga chegar a um buraco, ele precisa que
# a distância dele para o buraco seja menos que a metade da distância
# da raposa para o buraco.
def rabbitEscapes(cRabbit, cFox, cHole): # Recebe as coordenadas
    distRabbit = sqrt((cHole[0] - cRabbit[0])**2 + (cHole[1] - cRabbit[1])**2)
    distFox = sqrt((cHole[0] - cFox[0])**2 + (cHole[1] - cFox[1])**2)
    if distRabbit < (distFox / 2):
        return True
    else:
        return False

qtdHoles = int(input())
coordRabbit = [float(x) for x in input().split()]
coordFox = [float(x) for x in input().split()]
coordHoles = []

for i in range(qtdHoles):
    coordHoles += [[float(x) for x in input().split()]]

coelhoEscapa = False

# Agora que temos as coordenadas, testamos cada uma para a distância.
for hole in coordHoles:
    if rabbitEscapes(coordRabbit, coordFox, hole):
        coelhoEscapa = True
        print(f"O coelho pode escapar pelo buraco ({hole[0]:.3f}, {hole[1]:.3f}).")
        break
        
if not coelhoEscapa:
    print("O coelho nao pode escapar.")