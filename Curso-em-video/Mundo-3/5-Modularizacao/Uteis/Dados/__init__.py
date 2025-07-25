def leiaDinheiro(mensagem):
    while True:
        valor = input(mensagem)

        try:
            preco = float(valor)
            return preco
        except ValueError:
            print(f'\033[31mERRO! "{valor}" é um preço inválido.\033[m')