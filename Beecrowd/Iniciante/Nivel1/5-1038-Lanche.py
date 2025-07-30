def geraDicionario():
    precos = {
        1: 4.00,
        2: 4.50,
        3: 5.00,
        4: 2.00,
        5: 1.50
    }
    return precos

def main():
    cardapio = geraDicionario()
    codigo, quantidade = map(int, input().split())

    total = cardapio[codigo] * quantidade

    print(f'Total: R$ {total:.2f}')

main()