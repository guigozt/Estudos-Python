def imprime(p, i, po, n):
    print(f'{p} valor(es) par(es)')
    print(f'{i} valor(es) impar(es)')
    print(f'{po} valor(es) positivo(s)')
    print(f'{n} valor(es) negativo(s)')

def main():
    pares, impares, positivos, negativos = 0, 0, 0, 0

    for _ in range(5):
        valor = int(input())

        if valor % 2 == 0:
            pares += 1
        else:
            impares += 1

        if valor > 0:
            positivos += 1
        elif valor < 0:
            negativos += 1

    imprime(pares, impares, positivos, negativos)

main()