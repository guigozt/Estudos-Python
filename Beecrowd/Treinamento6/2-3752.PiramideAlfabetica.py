def piramide(q, t):
    if q == 'maiusculas':
        alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    else:
        alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for i in range(1, q+1):     
        letras = alfabeto[ : i] #Vai pegar cada letra: a -> b -> c...
        pontos = '.' * (26 - i) #Ex: 26 - 2: vai imprimir 24 '.' 
        linha = pontos + letras #Ex: 24 pontos + 2 letras (no final)
        print(linha)
        

def main():
    qtdLetras, tipo = input().split()
    qtdLetras = int(qtdLetras)

    piramide(qtdLetras, tipo)

main()
