def main():
    numInicial = int(input('Digite o 1º numero: '))
    posicao = 1
    maior = numInicial
    
    for cont in range(2,6):
        numProximo = int(input(f'Digite o {cont}º número: '))

        if numProximo > numInicial:
            posicao = cont
            maior = numProximo

            numInicial = numProximo

    print(f'{maior}')
    print(f'{posicao}')

main()
