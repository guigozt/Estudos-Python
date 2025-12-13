def main():
    soma = 0

    for i in range(6):
        valor = int(input('Valor: '))

        if valor % 2 == 0:
            soma += valor

    print('Soma somente dos valores pares:', soma)

main()