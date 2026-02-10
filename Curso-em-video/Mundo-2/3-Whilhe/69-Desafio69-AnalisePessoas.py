def main():
    quantHomem = 0
    quantMulheres = 0
    quantMaiores = 0

    while True:
        print('CADASTRE UMA PESSOA')
        print('-' * 19)

        idade = int(input('Informe a idade: '))
        
        while True:
            sexo = input('Informe o sexo (M/F): ').upper().strip()

            if sexo in 'MF':
                break
            print('Apenas os valores M ou F permitidos, tente novamente...')
        
        if idade > 18:
            quantMaiores += 1

        if sexo == 'M':
            quantHomem += 1
        elif sexo == 'F' and idade < 18:
            quantMulheres += 1

        continua = input('Quer continuar? (S/N): ').upper().strip()

        if continua == 'N':
            break

    print('\nANALISE DAS PESSOAS CADASTRADAS')
    print('-' * 31)

    print(f'{quantMaiores} maior(es) de idade foram registrada(s).')
    print(f'{quantHomem} homem(s) foram registrado(s).')
    print(f'{quantMulheres} mulher(es) menor de 20 anos foram registrada(s).')
    print()

main()