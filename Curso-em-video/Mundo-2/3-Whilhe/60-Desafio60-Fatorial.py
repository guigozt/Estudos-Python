def main():
    valor = int(input('Digite um valor: '))
    fatorial = 1

    contador = valor

    print(f'{valor}! = ', end=' ')

    while contador > 0:
        print(contador, end=' x ' if contador > 1 else ' = ')
        fatorial *= contador
        contador -= 1

    print(fatorial)

main()