def main():
    velocidade = float(input('QUal é a velocidade do seu veiculo? '))

    if velocidade > 80:
        print('MULTADO! Você excedeu o limite permitido de 80 km/h')
        multa = (velocidade - 80) * 7

        print(f'Você deve pagar uma multa de R$ {multa:.2f}!')

    print('Tenha um bom dia, e dirija com segurança')
        
main()
