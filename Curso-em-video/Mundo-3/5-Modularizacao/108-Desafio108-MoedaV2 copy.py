def main():
    import Moeda
    
    preco = float(input('Digite o preço (R$): '))

    print(f'A metade de {Moeda.formatacao(preco)} é: {Moeda.formatacao(Moeda.metade(preco))}')
    print(f'O dobro de {Moeda.formatacao(preco)} é: {Moeda.formatacao(Moeda.dobro(preco))}')
    print(f'Aumentando 10%, temos: {Moeda.formatacao(Moeda.aumento(preco, 10))}')
    print(f'Reduzindo 13%, temos: {Moeda.formatacao(Moeda.diminui(preco, 13))}')
    
main()