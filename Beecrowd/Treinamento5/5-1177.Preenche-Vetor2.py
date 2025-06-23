def preenche(L, v, t):
    for i in range(t):
        L[i] = i % v #Ex: 0%3=0 -> 1%3=1 -> 2%3=2 -> 3%3=0 -> 4%3=1...(reinicia o ciclo até o fim da lista)     

def exibe(L, t):
    for posicao, item in enumerate(L[ : t]):
        print(f'N[{posicao}] = {item}')

def main():
    valor = int(input('Valor: '))
    tamanho = 10
    L = [0] * tamanho

    preenche(L, valor, tamanho)
    exibe(L, tamanho)

main()
