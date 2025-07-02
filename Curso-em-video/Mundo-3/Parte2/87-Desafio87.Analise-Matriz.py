def main():
    matriz = []

    for L in range(3): #Linhas
        novaLinha = [] #Guarda os valores de cada linha

        for C in range(3): #Colunas
            valor = int(input(f'Digite um valor para a linha [{L}] | coluna [{C}]: '))
            novaLinha.append(valor)
        matriz.append(novaLinha) #Recebe cada linha da interação

    print('\n------ Matriz ------\n')
    
    for linha in matriz:
        for valor in linha: #Acessa cada valor da linha, ideial para formatar
            print(f'[{valor:^5}]', end='')
        print() #Pula linha

    print('-' * 20)

    soma = 0
    for linha in matriz:
        for valor in linha:
            if valor % 2 == 0:
                soma += valor
                
    print(f'A soma dos valores pares é de: {soma} ')

    somaColuna = 0
    for linha in matriz:
        somaColuna += linha[2] #Acessa a coluna da linha respectiva

    print(f'A soma dos valores da terceira coluna é: {somaColuna}')

    maior = max(matriz[1])
    print(f'O maior valor da segunda linha é: {maior}')

    
main()
