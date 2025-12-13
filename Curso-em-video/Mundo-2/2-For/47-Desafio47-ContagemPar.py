def main():
    print('INTERVALO [1 - 50]')
    print('-'* 18)

    for i in range(1, 50+1):
        if i % 2 == 0: 
            print(f'{i} é PAR')
    print('\nFIM...')

main()