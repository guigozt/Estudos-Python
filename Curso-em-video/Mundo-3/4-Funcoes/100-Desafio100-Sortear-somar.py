from random import randint
from time import sleep

def geraLista():
    L = [randint(1, 10) for _ in range(5)] #Outra forma: for i in range(5): -> ->L.append(randint(1, 10))
    return L

def imprimeNumeros(L):
    qtdNumeros = len(L)
    print(f'Sorteando {qtdNumeros} números da lista: ', end=' ')

    for valor in L:
        print(valor, end=' ', flush=True)
        sleep(0.4)

def somaPar(L):
    #Para cada valor iem L -> Se valor for par -> Retorna valor -> Soma entre eles
    somaPares = sum(valor for valor in L if valor % 2 == 0)

    print(f'\nSomando os valores pares de {L}, temos: {somaPares}')

def main():
    lista = geraLista()
    imprimeNumeros(lista)
    somaPar(lista)

main()