def main():
    termo = int(input('Termo: '))
    razao = int(input('Razão: '))
    pa = termo

    contador = 0

    while contador < 10:
        print(pa, end=' -> ')
        pa += razao
        contador += 1

    print('FIM...')

main()