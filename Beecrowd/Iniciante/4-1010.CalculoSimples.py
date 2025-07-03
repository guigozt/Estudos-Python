def main():
    codigo1, qtd1, valor1 = input().split()
    qtd1, valor1 = int(qtd1), float(valor1)

    codigo2, qtd2, valor2 = input().split()
    qtd2, valor2 = int(qtd2), float(valor2)

    totalPagar = (valor1 * qtd1) + (valor2 * qtd2)

    print(f'VALOR A PAGAR: R$ {totalPagar:.2f}')

main()
