from math import factorial

def fatorial(num, show=False): #Show como parametro opcional
    """Função fatoria(num, show=False) -> num: Valor a ser calculado | show: Parâmetro opcional para imprimir ou não o processo"""
    fat = 1
    if show: #Se show for verdadeiro
        print('Processo do fatorial: ', end=' ')

        for i in range(num, 0, -1): #Começa de [num] e vai até 0
            print(i, end=' x ' if i > 1 else ' = ')
            fat *= i #Ex: 1 * 5 = 5 -> 5 * 4 = 20 -> 20 * 3 = 60...
        print(fat)
        return fat #Neste caso, é preciso de um retorno, por causa do print no main
    else:
        return factorial(num)

def main():
    print(f'Resultado do fatorial: {fatorial(5, True)}')

main()