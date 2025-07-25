def main():
    import Moeda
    
    preco = float(input('Digite o preço (R$): '))

    print(f'A metade de {Moeda.formatacao(preco)} é: {Moeda.metade(preco, True)}')
    print(f'O dobro de {Moeda.formatacao(preco)} é: {Moeda.dobro(preco, True)}')
    print(f'Aumentando 10%, temos: {Moeda.aumento(preco, 10, True)}')
    print(f'Reduzindo 13%, temos: {Moeda.diminui(preco, 13, True)}')
        
main()