def main():
    salario = float(input('Qual o salário do funcionário? '))
    porc1 = 0.1
    porc2 = 0.15

    if salario > 1250:
        salario += salario * porc1
        print(f'O salário com aumento de 10% = R$ {salario:.2f}')
    else:
        salario += salario * porc2
        print(f'O salário com aumento de 15% = R$ {salario:.2f}')

main()
