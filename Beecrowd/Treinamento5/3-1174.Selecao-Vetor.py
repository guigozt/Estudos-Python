def geraLista(tam):
    L = []
    for i in range(tam):
        L.append(float(input('Valor: ')))
    return L

def exibe(L):
    i = 0
    print('------------------------')
    while i < len(L):
        if L[i] <= 10:
            print(f'A[{i}] = {L[i]}')
        i += 1

def main():
    lista = geraLista(100)
    exibe(lista)

main()
