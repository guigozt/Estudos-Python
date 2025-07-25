def main():
    from Uteis import Moeda
    preco =float(input('Preço (R$): '))
    Moeda.resumo(preco, 80, 35)
    
main()