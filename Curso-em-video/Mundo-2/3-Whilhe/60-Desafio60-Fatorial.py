def main():
    valor = int(input('Digite um valor: '))
    fatorial = 1

    contador = 1

    print(f'{valor}! = ', end=' ')

    while contador <= valor:
        print(contador, end=' x ' if contador < valor else ' ')
        fatorial *= contador
        contador += 1

    print(' = ', fatorial)

main()