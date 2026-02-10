def main():
    print('CAIXA ELETRÔNICO')
    print('-' * 16)

    valorSaque = int(input('Que valor você deseja sacar?: '))
    total = valorSaque

    cedula = 50
    totalCedula = 0

    while True:
        if total >= cedula:
            total -= cedula
            totalCedula += 1
        else:
            if totalCedula > 0:
                print(f'Total de {totalCedula} cédula(s) de R$ {cedula:.2f}')

            if cedula == 50:
                cedula = 20
            elif cedula == 20:
                cedula = 10
            elif cedula == 10:
                cedula = 1
            totalCedula = 0

            if total == 0:
                break

    print('-' * 16)
    print('Obrigado, volte sempre...')

main()