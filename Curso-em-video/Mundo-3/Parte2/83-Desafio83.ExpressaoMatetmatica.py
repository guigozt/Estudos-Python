def main():
    expressao = input('Expressão: ')
    cont = 0

    for caractere in expressao:
        if caractere == '(':
            cont += 1
        elif caractere == ')':
            cont -= 1

            if cont < 0: #Se tentar fechar sem abrir ")("
                print('Expressão inválida!')
                return

    if cont == 0:
        print('Expressao válida!')
    else:
        print('Expressao inválida')

main()
