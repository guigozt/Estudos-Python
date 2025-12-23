def main():
    peso = float(input(f'Digite o peso de uma pessoa: '))
    maior = peso
    menor = peso

    for i in range(4):
        peso = float(input(f'Digite o peso de outra pessoa: '))

        if peso > maior:
            maior = peso
        
        if peso < menor:
            menor = peso

    print()
    print(f'O maior peso entre os digitados é de: {maior:.2f} KG')
    print(f'O menor peso entre os digitados é de: {menor:.2f} KG')

main()