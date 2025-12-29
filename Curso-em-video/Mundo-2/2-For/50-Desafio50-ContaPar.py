def main():
    soma = 0

    for i in range(1, 6+1):
        valor = int(input(f'{i}º Valor: '))

        if valor % 2 == 0:
            soma += valor

    print('Soma somente dos valores pares:', soma)

main()