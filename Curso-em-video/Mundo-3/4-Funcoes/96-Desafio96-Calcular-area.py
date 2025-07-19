def area(larg, comp):
    areaTerreno = larg * comp
    print(f'A área de um terreno {larg:.1f} x {comp:.1f} é {areaTerreno:.1f}m²')

def main():
    print('Controle de Terrenos')
    print('-' * 20)

    largura = float(input('LARGURA (m): '))
    comprimento = float(input('COMPRIMENTO (m): '))

    area(largura,comprimento)

main()