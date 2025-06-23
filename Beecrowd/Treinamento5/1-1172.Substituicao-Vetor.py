def preenche(L): #Adiciona os valores nas posições
    for i in range(len(L)):
        valor = int(input('Valor: '))
        L[i] = valor 

def transforma(L): #Altera valores negativos para 1 dentro da lista
    i = 0
    while i < len(L):
        if L[i] <= 0:
            L[i] = 1
        i += 1

def exibe(L):
    print('--------------------')
    for i in range(len(L)):
        print(f'X[{i}] = {L[i]}')
        #       Indice    Valor

def main():
    lista = 10 * [0] #Cria uma lista com 10 posições iniciadas com 0
    preenche(lista)
    transforma(lista)
    exibe(lista)
    
main()
