def piramide(q, t):
    if t == 'maisculas':
        alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    else:
        alfabeto = 'abcdefghijklmnopqrstuvwxyz'

    for i in range(1, q+1):
        letras = alfabeto[:i]
        pontos = '.' * (26 - i)
        linha = pontos + letras
        print(linha)

def main():
    qtdLetras, tipo = input('Quantidade e tipo das letras: ').split()
    qtdLetras = int(qtdLetras)

    piramide(qtdLetras, tipo)

main()
