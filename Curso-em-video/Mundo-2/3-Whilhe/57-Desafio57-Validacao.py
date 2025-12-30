def main():   
    while True:
        sexo = input('Sexo (M/F): ').upper().strip()

        if sexo not in 'MF':
            print('Informação inválida, tente novamente...')
            continue
        break

    sexoCompleto = 'Masculino' if sexo == 'M' else 'Feminino'
    print('Seu sexo é: ', sexoCompleto)

main()