def geraLista(va, tam):
    L = [va] #va ocupa a posição 0

    for i in range(1, tam): #Percorre a partir do 1, pq a 0 esta o {va}
        L.append(2 * L[-1]) #Acessa a posição anterior de L[i] e multiplica o dobro a cada loop

    return L

def exibeLista(L):
    i = 0
    while i < len(L):
        print(f'N[{i}] = {L[i]}')
        i += 1
    
def main():
    valor = int(input('Valor: '))

    lista = geraLista(valor, 10) #Valor e o tamanho da lista
    exibeLista(lista)

main()

