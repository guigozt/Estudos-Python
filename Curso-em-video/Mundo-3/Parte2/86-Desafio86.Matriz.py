def main():
    matriz = []

    for L in range(3): #Linhas
        linha = [] #Guarda os valores de cada linha

        for C in range(3): #Colunas
            valor = int(input(f'Digite um valor para a linha [{L}] | coluna [{C}]: '))
            linha.append(valor)
        matriz.append(linha) #Recebe cada linha da interação

    print('\n------ Matriz ------\n')
    
    for linha in matriz:
        for valor in linha: #Acessa cada valor da linha, ideial para formatar
            print(f'[{valor:^5}]', end='')
        print() #Pula linha
main()
