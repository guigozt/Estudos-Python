def main():
    cont = 1
    maior = -1
    posicao = 0

    while cont <= 5:
        num = int(input(f'Digite o {cont}º número: '))

        if num > maior:
            maior = num
            posicao = cont

        cont += 1

    print(f'Maior número: {maior}')
    print(f'Posição: {posicao}')

main()
