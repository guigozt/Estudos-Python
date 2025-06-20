def main():
    num = int(input('Digite um número: '))
    cont = 1
    fatorial = num
    
    while cont < num:
        fatorial *= cont
        print(f'{num} X {cont} = {fatorial}')
        cont += 1

    print(f'FATORIAL = {fatorial}')

main()
