def main():
    while True:
        numDigitado = int(input('Digite um número entre 0 e 20: '))

        if 0 <= numDigitado <= 20:
            print(f'Você digitou o número: {numeros[numDigitado]}')
        else:
            print('Número inválido. Tente novamente.')

main()
