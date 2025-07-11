def main():
    matriz = [[0,0,0], [0,0,0], [0,0,0]]

    for linha in range(3):
        for coluna in range(3):
            matriz[linha][coluna] = int(input(f'Valor para linha {linha} | coluna {coluna}: '))

    print('\n------ MATRIZ ------\n')

    for linha in range(3):
        for coluna in range(3):
            print(f'[{matriz[linha][coluna]:^5}]', end='')
        print()
    
main()
