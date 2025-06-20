def main():
    idade = int(input('Digite uma idade: '))
    contIdade = 0
    somaIdade = 0

    while idade > 0:
        somaIdade += idade
        contIdade += 1
        idade = int(input('Digite outra idade: '))

    print(f'{somaIdade / contIdade:.2f}')
    
main()
