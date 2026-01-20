def main():   
    while True:
        sexo = input('Sexo (M/F): ').upper().strip()

        if sexo in 'MF':
            break
        print('Informação inválida, tente novamente...')

    sexoCompleto = 'Masculino' if sexo == 'M' else 'Feminino'
    print('Seu sexo é: ', sexoCompleto)

main()