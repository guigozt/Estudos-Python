def main():
    valorCasa = float(input('Valor da Casa: '))
    salario = float(input('Salário: '))
    anosPagamento = int(input('Quanto anos deseja parcelar?: '))
    
    parcelaMaxima = salario * 0.30
    meses = anosPagamento * 12
    parcelas = valorCasa / meses

    print(f'Valor máximo das parcelas: R$ {parcelaMaxima:.2f}')
    print(f'Valor das Parcelas: R$ {parcelas:.2f} por {meses} meses')

    if parcelas > parcelaMaxima:
        print('\nCOMPRA NÃO APROVADA')
    else:
        print('\nCOMPRA APROVADA')

main()