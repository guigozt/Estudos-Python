def geraLista(tam):
    L = []

    for i in range(tam):
        L.append(int(input('Valor: ')))
        
    return L

def troca(L, i, j):
    aux = L[i]
    L[i] = L[j]
    L[j] = aux

def inverte(L):
    i = 0
    j = len(L) - 1

    while i < j:
        troca(L, i, j)
        i += 1
        j -= 1

def exibe(L):
    print('--------------------')
    for i in range(len(L)):
        print(f'N[{i}] = {L[i]}')

def main():
    L = geraLista(10)
    inverte(L)
    exibe(L)

main()
