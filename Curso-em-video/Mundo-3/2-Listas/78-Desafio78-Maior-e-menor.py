def main():
    lista=[]
    
    for i in range(1, 6):
        lista.append(int(input(f'Digite um valor para a posição [{i}]: ')))

    maior = max(lista)
    menor = min(lista)

    print('-' * 10)
    print(f'O maior número da lista é: {maior} nas posições: ', end='')
    for i, v in enumerate(lista):
        i += 1
        if v == maior:  #Percorre a lista para procurar as posições do maior número(caso ele apareca mais de uma vez)
            print(f'{i}...', end='')
    print()
    print(f'O menor número da lista é: {menor} nas posições: ', end='')
    for i, v in enumerate(lista):
        i += 1
        if v == menor:  #Percorre a lista para procurar as posições do menor número(caso ele apareca mais de uma vez)
            print(f'{i}...', end='')

main()

