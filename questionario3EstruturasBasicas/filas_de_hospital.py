class Fila:
    def __init__(self):
        self.items = []

    def vazia(self):
        return self.items == []

    def enfileirar(self, item):
        self.items.insert(0, item)
        senha = self.tamanho()

    def desenfileirar(self):
        return self.items.pop()

    def tamanho(self):
        return len(self.items)

    def indice(self, item):
        return self.items.index(item) + 1

    def getItems(self):
        return self.items

paciente = input()

fila = Fila()
fila_geral_original = Fila()
fila_preferencial = Fila()
fila_geral_atualizada = Fila()
res_fila_preferencial = Fila()
res_fila_geral = Fila()

senha = 0

while paciente:
    senha = senha + 1
    fila.enfileirar((int(paciente), senha))
    fila_geral_original.enfileirar((int(paciente), senha))
    paciente = input()

while not fila.vazia():
    item = fila.desenfileirar()
    if item[0] >= 60:
        fila_preferencial.enfileirar(item)
    else:
        fila_geral_atualizada.enfileirar(item)
        
f_original_idades = []
f_original_senhas = []

while not fila_geral_original.vazia():
    item = fila_geral_original.desenfileirar()
    f_original_idades.append(item[0])
    f_original_senhas.append(item[1])

f_pref = []
f_pref_res = []

while not fila_preferencial.vazia():
    item = fila_preferencial.desenfileirar()
    f_pref.append(item[0])
    f_pref_res.append(item[1])

f_atualizada = []
f_atualizada_res = []

while not fila_geral_atualizada.vazia():
    item = fila_geral_atualizada.desenfileirar()
    f_atualizada.append(item[0])
    f_atualizada_res.append(item[1])

print('Fila geral original')
for i in range(len(f_original_idades)):
    print(f'{i+1} - {f_original_idades[i]}')

print('')

print('Fila preferencial')
for i in range(len(f_pref)):
    print(f'{f_pref_res[i]} - {f_pref[i]}')

print('')

print('Fila geral atualizada')
for i in range(len(f_atualizada)):
    print(f'{f_atualizada_res[i]} - {f_atualizada[i]}')

print('')

print('Resultado esperado fila preferencial')
for i in range(len(f_pref_res)):
    print(f'{i+1} - {f_pref_res[i]}')

print('')

print('Resultado esperado fila geral')
for i in range(len(f_atualizada_res)):
    print(f'{i+1} - {f_atualizada_res[i]}')