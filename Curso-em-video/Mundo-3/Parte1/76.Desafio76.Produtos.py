def main():
    listagem = ('Lápis',1.75,'Borracha',2,'Caderno',15.90,'Estojo',25,'Transferidor',4.20,'Compasso',9.99,'Mochila',120.32,'Canetas',22.30,'Livro',34.90)

    print('-' * 40)
    print(f'{"LISTAGEM DE PREÇOS":^40}')
    print('-' * 40)
    
    for i in range(0, len(listagem), 2): #Percorre de 2 em 2
        produto = listagem[i] #ex: Lapis(0) -> Borracha(3)
        preco = listagem[i+1] #ex: 1.75(1) -> 2(4)
        print(f'{produto:.<30} R$ {preco:>6.2f}')
    print('-' * 40)
    
main()
