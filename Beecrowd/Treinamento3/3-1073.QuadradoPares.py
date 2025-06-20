from math import sqrt

def quadrado(n):
    i = 1

    while i <= n:
        if i % 2 == 0:                
            print(f'{i}^2 = {i**2}')
        i += 1
    
def main():
    num = int(input('Digite um número: '))

    quadrado(num)

main()
