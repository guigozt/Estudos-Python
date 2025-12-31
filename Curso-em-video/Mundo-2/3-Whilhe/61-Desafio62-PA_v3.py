def main():
    termo = int(input('Termo: '))
    razao = int(input('Razao: '))
    pa = termo
    contador = 0

    while contador < 10:
        print(pa, end=' -> ' if contador < 9 else ' ')
        pa += razao
        contador += 1
    
    while True:
        termosAdicionais = int(input('\nVocê quer mostrar mais quantos termos? (0 para encerrar): '))

        if termosAdicionais >= 0:
            break
        print('Valor inválido, tente novamente...')
        
    if termosAdicionais == 0:
        print('Obrigado por utilizar...')
    else:
        cont = 0
        while cont < termosAdicionais:
            print(pa, end=' -> ' if cont < termosAdicionais - 1 else ' ')
            pa += razao
            cont += 1

main()