def main():
    lista = [[],[]] #lista[0] -> pares / lista[1] -> impares

    for i in range(1, 8):
        valor = int(input(f'{i}º Valor: '))

        if valor % 2 == 0:
            lista[0].append(valor)
        else:
            lista[1].append(valor)

    lista[0].sort()
    lista[1].sort()

    if not lista[0] and lista[1]: #Se lista[0] estiver vazia e lista[1] existir...
        print('Não foram inseridos valores pares na lista')
        print(f'Valores impares: {lista[1]}')
    elif lista[0] and not lista[1]: #Se lista[0] existir e lista[1] estiver vazia...
        print(f'Valores pares: {lista[0]}')
        print('Não foram inseridos valores impares na lista')
    else: #Se as duas existirem...
        print(f'Valores pares: {lista[0]}')
        print(f'Valores impares: {lista[1]}')

main()

