def main():
    from math import hypot
    catetoOposto = float(input('Qual o comprimento do cateto oposto: '))
    catetoAdjacente = float(input('Qual o comprimento do cateto adjacente: '))

    hipotenusa = hypot(catetoOposto, catetoAdjacente)

    print(f'A hipotenusa mede: {hipotenusa:.2f}')

main()
