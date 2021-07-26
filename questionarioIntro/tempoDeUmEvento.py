# Crie um programa que calcule a duração total de um evento sabendo
# o dia, hora, minutos e segundos para as datas inicial e final
# Formato: dia hora:minuto:segundo
inicio = input()
fim = input()

inicio = inicio.split() # dia = inicio[0]
inicio = [inicio[0]] + inicio[1].split(':') # transformar o segundo elemento em lista
inicio = [int(x) for x in inicio] # transformar em int

# Fazer o mesmo para `fim`
fim = fim.split() 
fim = [fim[0]] + fim[1].split(':')
fim = [int(x) for x in fim]

# Atribuir as variáveis
diaInicio, horaInicio, minutoInicio, segundoInicio = inicio
diaFim, horaFim, minutoFim, segundoFim = fim

cond1 = diaFim < diaInicio
cond2 = inicio[0] == fim[0] and horaFim < horaInicio
cond3 = inicio[0:1] == fim[0:1] and minutoFim < minutoInicio
cond4 = inicio[0:2] == fim[0:2] and segundoFim < segundoInicio
cond5 = fim == inicio

if cond1 or cond2 or cond3 or cond4 or cond5:
    print("Data inválida!")
else:
    dias = diaFim - diaInicio
    horas = horaFim - horaInicio
    minutos = minutoFim - minutoInicio
    segundos = segundoFim - segundoInicio

    if segundos < 0:
        minutos -= 1
        segundos += 60
    if minutos < 0:
        horas -= 1
        minutos += 60
    if horas < 0:
        dias -= 1
        horas += 24

    print(f"{dias} dia(s)")
    print(f"{horas} hora(s)")
    print(f"{minutos} minuto(s)")
    print(f"{segundos} segundo(s)")
