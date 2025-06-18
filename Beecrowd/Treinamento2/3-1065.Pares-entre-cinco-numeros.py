def pares(v1, v2, v3, v4, v5):
    qtdPares = 0
    
    if v1 % 2 == 0:
        qtdPares += 1

    if v2 % 2 == 0:
        qtdPares += 1

    if v3 % 2 == 0:
        qtdPares += 1

    if v4 % 2 == 0:
        qtdPares += 1

    if v5 % 2 == 0:
        qtdPares += 1

    return qtdPares
        

def main():
    valor1 = int(input('Valor 1: '))
    valor2 = int(input('Valor 2: '))
    valor3 = int(input('Valor 3: '))
    valor4 = int(input('Valor 4: '))
    valor5 = int(input('Valor 5: '))

    print(f'{pares(valor1, valor2, valor3, valor4, valor5)} valores pares')
    
main()
