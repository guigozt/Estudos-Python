def main():
    class Carro:
        velocidadeMax = 0
        cor = ''
        ligado = False

    carro1 = Carro()

    carro1.velocidadeMax = 100
    carro1.cor = 'Preto'
    estado = 'Sim' if carro1.ligado else 'Não'

    print('\nObjeto Carro1\n')
    print(f'Velocidade Máxima: {carro1.velocidadeMax}')
    print(f'Cor: {carro1.cor}')
    print(f'Estado: {estado}')

main()