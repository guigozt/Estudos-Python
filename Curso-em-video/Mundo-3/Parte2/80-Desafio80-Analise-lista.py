def main():
    lista = []

    while True:
        valor = int(input('Digite um valor: '))
        lista.append(valor)
        op = input('Deseja continuar? [S/N] ').strip().lower()

        if op != 's':
            break

    print(f'Você digitou {len(lista)} elementos')
    lista.sort(reverse=True)
    print(f'Os valores em ordem descrescente são: {lista}')

    if 5 in lista:
        print('O valor 5 faz parte da lista!')
    else:
        print('O valor 5 não faz parte da lista!')    

main()
