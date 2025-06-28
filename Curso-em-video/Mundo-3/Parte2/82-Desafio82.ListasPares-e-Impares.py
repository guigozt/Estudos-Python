def main():
    lista = []
    listaPares = []
    listaImpares = []

    while True:
        valor = int(input('Digite um valor: '))
        lista.append(valor)
        op = input('Deseja continuar? [S/N] ').strip().lower()

        if op != 's':
            break

    for p, v in enumerate(lista):
        if v % 2 == 0:
            listaPares.append(v)
        else:
            listaImpares.append(v)

    print(f'A lista completa é: {lista}')
    print(f'A lista de pares é: {listaPares}')
    print(f'A lista de impares é: {listaImpares}')

main()
