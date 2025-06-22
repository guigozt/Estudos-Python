def main():
    distanciaViagem = float(input('Qual é a distancia da sua viagem (KM): '))
    preco1 = 0.50
    preco2 = 0.45
    precoViagem = 0
    
    if distanciaViagem <= 200:
        precoViagem = preco1 * distanciaViagem
    else:
        precoViagem = preco2 * distanciaViagem

    print(f'Sua viagem de {distanciaViagem} KM vai custar R$ {precoViagem:.2f}')

main()

