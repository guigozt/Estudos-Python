def leiaDinheiro(mensagem):
    while True:
        valor = input(mensagem).replace(',','.').strip() #Troca diretamente os pontos por virgula

        if valor.isalpha() or valor == '': #Verfica se é alfanumérico ou se está vazio
            print(f'\033[31mERRO! "{valor}" é um preço inválido.\033[m')
        else:
            preco = float(valor)
            return preco