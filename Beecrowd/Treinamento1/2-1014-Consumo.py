def consumo(km, comb):
    return km / comb

def main():
    km = int(input('Distância(KM): '))
    combustivel = float(input('Combustível: '))

    print(f'Consumo médio: {consumo(km, combustivel):.3f} km/l')

main()
