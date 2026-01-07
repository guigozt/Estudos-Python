def main():
    qtdNumeros = 0
    somaNumeros = 0

    while True:
        numero = int(input('Digite um número (999 Interromper): '))

        if numero == 999:
            break
        qtdNumeros += 1
        somaNumeros += numero

    print('\nANALISE DO PROGRAMA')
    print('-' * 19)
    print('Você digitou: ',qtdNumeros,'números')
    print('A soma entre eles é: ', somaNumeros)

main()