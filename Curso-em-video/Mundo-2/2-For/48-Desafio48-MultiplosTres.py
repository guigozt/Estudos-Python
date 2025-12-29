def main():
    soma = 0
    cont = 0

    for i in range(1, 500+1, 2):
        if i % 3 == 0:
            soma += i
            cont += 1

    print(f'A soma dos {cont} números impares multiplos de três digitados é de: {soma}')

main()