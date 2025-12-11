def menuPagamento():
    print('ESCOLHA A OPÇÃO DE PAGAMENTO')
    print('-' * 28)
    print('[1] A vista no dinheiro/cheque')
    print('[2] A vista no cartão')
    print('[3] Parcelado em 2x no cartão')
    print('[4] Parcelado em 3x no cartão')
    opcao = int(input('Opção: '))
    return opcao

def formaPagamento(preco, op):
    pagamento = {
        1: preco - (preco * 0.1),
        2: preco - (preco * 0.05),
        3: preco,
        4: preco + (preco * 0.2)
    }

    if op in pagamento:
        print('Pagamento realizado com sucesso')
        print(f'Valor Final: R$ {pagamento[op]:.2f}')
    else:
        print('Não foi possível realizar pagamento')

def main():
    preco = float(input('Preço (R$): '))
    opcaoEscolhida = menuPagamento()

    formaPagamento(preco, opcaoEscolhida)

main()