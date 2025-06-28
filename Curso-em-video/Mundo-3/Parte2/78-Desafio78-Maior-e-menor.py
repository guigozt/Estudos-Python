def main():
    lista=[]
    
    for i in range(1, 6):
        lista.append(int(input(f'Digite um valor para a posição [{i}]: ')))

    maior = max(lista)
    posicaoMaior = lista.index(maior)+1
    
    menor = min(lista)
    posicaoMenor = lista.index(menor)+1

    print('-' * 10)
    print(f'O maior número da lista é: {maior} na posição {posicaoMaior}')
    print(f'O menor número da lista é: {menor} na posição {posicaoMenor}')

main()

