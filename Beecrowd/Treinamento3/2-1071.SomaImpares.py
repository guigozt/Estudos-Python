def main():
    inicio = int(input('Valor 1: '))
    fim = int(input('Valor 2: '))

    aux = 0
    somaImpares = 0

    if inicio > fim:
        aux = inicio
        inicio = fim
        fim = aux

    cont = inicio + 1

    while cont < fim:     
        if cont % 2 != 0:
            somaImpares += cont
        cont += 1

    print(somaImpares)

main()
