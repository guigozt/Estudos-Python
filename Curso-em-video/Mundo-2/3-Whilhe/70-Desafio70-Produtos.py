def main():
    nomeMenorProduto = ''
    precoMenorProduto = 0
    quantMaiorMil = 0
    totalGasto = 0

    print('CADASTRO DE PRODUTOS')
    print('-' * 12)

    nomeProduto = input('Nome do Produto: ')
    precoProduto = float(input('Preço (R$): '))

    nomeMenorProduto = nomeProduto
    precoMenorProduto = precoProduto
    totalGasto += precoProduto

    if precoProduto > 1000.0:
        quantMaiorMil += 1

    while True:
        opcao = input('Deseja continuar? (S/N): ').upper().strip()

        if opcao == 'N':
            break

        nomeProduto = input('Nome do Produto: ')
        precoProduto = float(input('Preço (R$): '))

        if precoProduto <= precoMenorProduto:
            nomeMenorProduto = nomeProduto
            precoMenorProduto = precoProduto
        
        totalGasto += precoProduto

        if precoProduto > 1000.0:
            quantMaiorMil += 1

    print('\nANALISE DOS PRODUTOS CADASTRADOS')        
    print('-' * 32)

    print(f'Total da compra: R$ {totalGasto:.2f}')
    print(f'{quantMaiorMil} produto(s) custam mais de R$ 1000,00')
    print(f'O produto mais barato: {nomeMenorProduto} - R$ {precoMenorProduto:.2f}')
    print()

main()