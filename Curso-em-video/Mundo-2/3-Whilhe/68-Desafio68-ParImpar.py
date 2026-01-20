from random import randint

def main():
    print('VAMOS JOGAR PAR OU IMPAR')
    quantVencedor = 0

    while True:
        print('-' * 24)

        opcaoJogador = input('Você escolhe PAR ou IMPAR? [P/I]: ').upper().strip()
        valorJogador = int(input('Escolha um valor para jogar: '))

        valorMaquina = randint(0, 10)
        resultado = valorJogador + valorMaquina

        print('-' * 24)
        print(f'Você jogou {valorJogador} e a máquina jogou {valorMaquina}')
        print(f'Total: {resultado}', end=' -> ')

        vencedor = ''

        if resultado % 2 == 0:
            print('DEU PAR')
            vencedor = 'P'
        else:
            print('DEU IMPAR')
            vencedor = 'I'

        if opcaoJogador == vencedor:
            print('\nVocê VENCEU!')
            quantVencedor += 1
            print('Vamos jogar novamente...')
        else:
            print('\nVocê PERDEU')
            print('GAME OVER...')
            break
    
    print('-' * 24)
    print(f'Você venceu {quantVencedor} vez(es)')
    
main()