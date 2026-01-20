def main():
    while True:
        valor = int(input('Quer ver a tabuada de qual valor? '))
        print('-' * 34)

        if valor < 1:
            break

        cont = 0
        while cont <= 10:
            print(f'{valor} X {cont} = {valor * cont}')
            cont += 1
    
    print('Tabuada encerrada...')

main()