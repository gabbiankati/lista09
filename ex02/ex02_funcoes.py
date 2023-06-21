def receber_entrada() -> list:
    entrada = []

    for i in range(5):
        num = int(input(f'Informe o valor da posição {i}: '))
        entrada.append(num)
    return entrada

def gerar_saida(entrada: list) -> list:
    saida = []

    for i in range(len(entrada)):

        if i % 2 == 0:
            saida.append(entrada[i] * 2)
        else:
            saida.append(entrada[i] * 3)
    return saida

