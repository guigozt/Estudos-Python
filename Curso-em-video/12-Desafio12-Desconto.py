valor = float(input('Digite o valor de uma compra (R$): '))
desconto = valor - (valor * 5/100)

print(f'A compra com 5% de desconto é igual a: R$ {desconto:.2f}')
