import time


def soma_ate(n):
    resultado = 0
    for i in range(1, n + 1):
        resultado = resultado + 1
    return resultado


# Código muito menos legível, porém que implementa o mesmo algoritmo
def naboo(midichlorian):
    jabba = 0
    for carbonita in range(1, midichlorian + 1):
        ewok = carbonita
        jabba += ewok
    return jabba

# Função da Leia
def soma_pa(n):
  return n * (1 + n) / 2

num_testes = 5
media = 0

for _ in range(num_testes):
    inicio = time.time()
    soma_ate(10000000)
    fim = time.time()

    tempo_de_execucao = fim - inicio
    media += tempo_de_execucao
    print(f'Tempo soma_ate: {tempo_de_execucao}')

    inicio = time.time()
    soma_pa(10000000)
    fim = time.time()

    tempo_de_execucao = fim - inicio
    print(f'Tempo soma_pa: {tempo_de_execucao}')

media /= num_testes
print(f'Média de tempo: {media}')
