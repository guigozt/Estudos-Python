def main():
    quantNumeros = 0
    soma = 0

    while True:
        valor = int(input('Digite um valor (999 interrompe): '))

        if valor == 999:
            break

        quantNumeros += 1
        soma += valor

    print('ANALISE DO PROGRAMA')
    print('-' * 19)

    print('Quantidade de números digitados: ', quantNumeros)
    print('Soma dos números: ', soma)

main()