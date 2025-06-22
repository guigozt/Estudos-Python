def formaTriangulo(a, b, c):
    #Poderia retornar True ou False, mas dá pra simplificar
    
    return a + b > c and b + c > a and c + a > b

def tipoTriangulo(a, b, c):
    if a == b and c == a:               #Todos Iguais
        print('TRIANGULO EQUILATERO')
    elif a == b or a == c or b == c:    #Dois lados iguais
        print('TRIANGULO ISOSCELES')
    else:                               #Nenhum lado igual
        print('TRIANGULO ESCALENO')
    
def main():
    a, b, c = map(float, input('Digite 3 valores: ').split())

    if formaTriangulo(a, b, c):
        print('Forma um Triangulo!')
        tipoTriangulo(a, b, c)
    else:
        print('Não forma um Triangulo!')

main()
