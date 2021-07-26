# Exercício 7 - copy + paste
from math import ceil

fileSize = int(input()) # tamanho do arquivo em bytes

total_data_transferred = 0
data_transferred = 0
cycle_data = 0
count = 0
t_time = 0
t_remaining = 0

print(f"Transmitindo {fileSize} bytes...")

while total_data_transferred <= fileSize:
    data_transferred = int(input())
    t_time += 1
    count += 1
    total_data_transferred += data_transferred
    if total_data_transferred == fileSize:
        print(f"Tempo total: {t_time} segundos.")
        break
    if count < 5:
        cycle_data += data_transferred
    elif count == 5:
        count = 0
        cycle_data += data_transferred
        if cycle_data == 0:
            print("Tempo restante: pendente...")
        else:
            rate = cycle_data / 5
            t_remaining = ceil((fileSize - total_data_transferred) / rate)
            print(f"Tempo restante: {t_remaining} segundos.")
        cycle_data = 0

