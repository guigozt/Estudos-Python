def main():
    import Moeda
    
    preco = float(input('Digite o preço (R$): '))
    
    print(f'A metade de {preco} é: {Moeda.metade(preco)}')
    print(f'O dobro de {preco} é: {Moeda.dobro(preco)}')
    print(f'Aumentando 10%, temos: {Moeda.aumento(preco, 10)}')
    print(f'Reduzindo 13%, temos: {Moeda.diminui(preco, 13)}')
    
main()