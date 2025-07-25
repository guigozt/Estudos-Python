def main():
    from Uteis import Moeda, Dados
    preco = Dados.leiaDinheiro('Digite o preço (R$): ')
    Moeda.resumo(preco, 80, 35)
main()