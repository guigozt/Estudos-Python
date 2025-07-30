def esfera(r):
    pi = 3.14159
    return (4.0 / 3) * pi * r**3

def main():
    raio = int(input())
    print(f'VOLUME = {esfera(raio):.3f}')
main()