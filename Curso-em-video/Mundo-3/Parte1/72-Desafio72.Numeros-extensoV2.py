def main():
    numeros = (
        'Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete',
        'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze',
        'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte'
    )
    
    while True:
        numDigitado = int(input('Digite um número entre 0 e 20: '))

        if 0 <= numDigitado <= 20:
            print(f'Você digitou o número: {numeros[numDigitado]}')
        else:
            print('Número inválido. Tente novamente.')

main()
