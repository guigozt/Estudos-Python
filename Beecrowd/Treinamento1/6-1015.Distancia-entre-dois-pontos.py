from math import sqrt

def distancia(x1,x2,y1,y2):
    return sqrt((x2-x1)**2 + (y2-y1)**2)

def main():
    x1, y1 = input('Digite os valores de x1 e y1: ').split()
    x2, y2 = input('Digite os valores de x2 e y2: ').split()

    x1 = float(x1)
    x2 = float(x2)
    y1 = float(y1)
    y2 = float(y2)

    print(f'A distancia entre os dois pontos é de: {distancia(x1,x2,y1,y2):.4f}')

main()
