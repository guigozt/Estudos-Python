def main():
    diaTrabalho = int(input('Dias trabalhados: '))
    contTrabalho = 0

    while contTrabalho < diaTrabalho:
        numFeedback = int(input('Quantos feedBacks teve no dia? '))

        for contFeedback in range(numFeedback):
            categoria = int(input('Digite a categoria: '))

            if categoria == 1:
                print('Rolien')
            elif categoria == 2:
                print('Naej')
            elif categoria == 3:
                print('Elehcim')
            else:
                print('Odranoel')

        contTrabalho += 1

main()
