#Escopo de variaveis -------------------------
def teste(b): #b = a -> 5
    global a #Informa que vai usar a variavel global [a], mas poderia criar uma variavel local [a], que seria diferente
    a = 8
    b += 4 #local
    c = 2 #local
    print(f'[a] dentro vale {a}')
    print(f'[b] dentro vale {b}')
    print(f'[c] dentro vale {c}')

a = 5 #Variavel global
teste(a) #Vai imprimir
print(f'[a] fora vale {a}') #Vai imprimir 8, pois foi alterada la na função

#Parametros opcionais ------------------------
def somar(a=0, b=0, c=0): #Inicializa os valores com 0, caso eles não sejam passados, não vão interferir na função
    s = a + b + c
    print(f'A soma é igual a {s}')

somar(a=2, b=4, c=2)
somar(a=2, b=4)
somar(c=6)
somar()

#DocStrings ----------------------------------
def contador(i, f, p):
    #Usada pra documentar a função, como um guia
    """ 
    -> Faz uma contagem e mostra na tela,
    i: inicio da contagem;
    f: final na contagem;
    p: passo da contagem;
    return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end= ' ')
        c += p
    print('FIM')

help(contador)

# Help e Doc ----------------------------------
help(print) #Para saber informações sobre o comando, no caso o print
print(input.__doc__) #Informações sobre o input

#Retorno de valores---------------------------
def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f #Retorna um valor para ser usado na principal

n = int(input('Numero: '))
print(f'O fatorial de n = {fatorial(n)}')
print()

f1 = fatorial(4)
f2 = fatorial()
print(f'Os resultados são {f1} e {f2}')
