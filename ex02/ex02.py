entrada = []

for i in range(5):
    num = int(input(f'Informe o valor da posição {i}: '))
    entrada.append(num)

saida = []
#percorre a lista de entrada de 0 até o tamanho
for i in range(len(entrada)):
    if i % 2 == 0:
        saida.append(entrada[i] * 2)#adiciona o dobro do valor na lista de entrada, na lista de saida
    else:
        saida.append(entrada[i] * 3)#adiciona o triplo do valor na lista de entrada, na lista de saida
print(saida)