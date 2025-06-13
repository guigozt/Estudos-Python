def areaTriangulo(a, c):
    return (a * c) / 2

def areaCirculo(c):
    return 3.14159 * c**2

def areaTrapezio(a, b, c):
    return (a + b) * c/2
    
def areaQuadrado(b):
    return b**2

def areaRetangulo(a, b):
    return a*b

def main():
    A, B, C = input().split()
    A = float(A)
    B = float(B)
    C = float(C)

    print(f'TRIANGULO: {areaTriangulo(A, C):.3f}')
    print(f'CIRCULO: {areaCirculo(C):.3f}')
    print(f'TRAPEZIO: {areaTrapezio(A, B, C):.3f}')
    print(f'QUADRADO: {areaQuadrado(B):.3f}')
    print(f'RETANGULO: {areaRetangulo(A, B):.3f}')

main()
