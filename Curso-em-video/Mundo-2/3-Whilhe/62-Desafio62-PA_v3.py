def main():
    termo = int(input('Termo: '))
    razao = int(input('Razao: '))
    pa = termo
    contador = 0
    total = 0
    termosAdicionais = 10

    while termosAdicionais != 0:
        total += termosAdicionais

        while contador < total:
            print(pa, end=' -> ')
            pa += razao
            contador += 1
        print('PAUSA...')
            
        termosAdicionais = int(input('\nVocê quer mostrar mais quantos termos? (0 para encerrar): '))
    print('FIM...')

main()