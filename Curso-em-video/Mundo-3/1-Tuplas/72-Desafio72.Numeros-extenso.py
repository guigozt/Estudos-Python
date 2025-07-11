def main():
    numeros = (
        'Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete',
        'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze',
        'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte'
    )

    while True:
        numDigitado = int(input('Digite um número entre 0 e 20: '))

        for posicao, valor in enumerate(numeros):
            if numDigitado == posicao:
                print(f'Você digitou o número: {valor}')
                break
        else:
            print('Ops! tente novamente. ', end='')

main()
