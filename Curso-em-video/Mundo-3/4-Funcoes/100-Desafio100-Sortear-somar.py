from random import randint
from time import sleep

def geraLista():
    L = [randint(1, 10) for _ in range(5)]
    return L

def imprimeNumeros(* numeros):
    qtdNumeros = len(numeros)
    print(f'Sorteando {qtdNumeros} números da lista: ', end=' ')

    for i, valor in enumerate(numeros):
        print(valor, end=' ', flush=True)
        sleep(0.4)

def somaPar(* numeros):
    somaPares = sum(valor for i, valor in enumerate(numeros) if valor % 2 == 0)

    print(f'\nSomando os valores pares de {numeros}, temos: {somaPares}')

def main():
    lista = geraLista()
    imprimeNumeros(* lista)
    somaPar(* lista)

main()