def formaTriangulo(a, b, c):
    return a + b > c and a + c > b and b + c > a

def tipoTriangulo(a, b, c):
    if a == b and b == c:
        print('TRIANGULO EQUILATERO')
    elif a == b or b == c or c == a:
        print('TRIANGULO ISOSCELES')
    else:
        print('TRIANGULO ESCALENO')

def main():
    a, b, c = map(float, input('Digite 3 valores: ').split())

    if formaTriangulo(a, b, c):
        print('Formam um Triangulo!')
        tipoTriangulo(a, b, c)
    else:
        print('Não formam um Triangulo')

main()