from time import sleep

def linha():
    print('-' * 30)

def contador(inicio, fim, passo):

    if passo == 0:
        passo = 1

    print(f'CONTAGEM DE {inicio} ATÉ {fim} -> DE {passo} EM {passo}: ')

    #Incio menor que fim (crescente)
    if inicio <= fim:
        for i in range(inicio, fim+1, abs(passo)): #abs para o passo não ser negativo 
            print(i, end=' ', flush=True) #flush=True -> força o print() a mostrar o número imediatamente (sem esperar o buffer)
            sleep(0.2)
    #Inicio maior que fim (decrescente)
    else:
        for i in range(inicio, fim+1, -abs(passo)):
            print(i, end=' ', flush=True)
            sleep(0.2)
    print()

def main():
    contador(1, 10, 1)
    linha()
    contador(10, 0, 2)

    print('\nAgora é a sua vez de personalizar a contagem!')
    inicio, fim, passo = map(int, input('Informe o INICIO | FIM | PASSO: ').split())
    linha()
    contador(inicio, fim, passo)

main()