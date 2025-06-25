def main():
    numero = tuple(int(input(f'Digite o {i+1}º número: ')) for i in range(4))
    
    print(f'Você digitou os números: {numero}')
    print(f'O número 9 apareceu {numero.count(9)} vezes')   

    if 3 in numero:
        print(f'O número 3 apareceu na {numero.index(3)+1}ª posicao')
    else:
        print(f'O numero 3 não apareceu em nenhuma posição')

    print('Os valores pares digitados foram', end=' ')
    
    for elemento in numero:
        if elemento % 2 == 0:
            print(elemento, end=' ')
    
main()
