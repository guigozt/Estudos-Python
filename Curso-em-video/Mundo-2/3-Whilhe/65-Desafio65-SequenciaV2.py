def main():
    numero = int(input('Digite um número: '))
    
    qtdNumeros = 1
    somaNumeros = numero
    maior = menor = numero

    while True:
        opcao = input('Quer continuar? (S/N): ').upper().strip()
        if opcao == 'N':
            break

        num = int(input('Digite outro número: '))

        qtdNumeros += 1
        somaNumeros += num
        
        if num > maior:
            maior = num

        if num < menor:
            menor = num

    print('\nANALISE DO PROGRAMA')
    print('-' * 19)
    print(f'MÉDIA: {somaNumeros / qtdNumeros:.2f}')
    print('MAIOR: ', maior)
    print('MENOR: ', menor)

main()