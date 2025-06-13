def bonus(sal, ven):
    return sal + (ven * 0.15)

def main():
    nome = input('Nome do vendedor: ')
    salario = float(input('Salário fixo: '))
    vendas = float(input('Vendas: '))

    print(f'TOTAL = R$ {bonus(salario, vendas):.2f}')
    
main()
