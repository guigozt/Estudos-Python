def multiplicacao(va, i):
    return va * i

def main():
    valor = int(input('Valor: '))
    print('TABUADA DO ', valor)
    print('-' * 15)

    for i in range(0, 10+1):
        print(f'{valor} X {i} = {multiplicacao(valor, i)}')

    print('FIM...')
main()