from random import randint

def main():
    numeroGerado = randint(0, 10)
    qtdTentativa = 0

    print('JOGO DA ADIVINHAÇÃO')
    print('-' * 19)

    while True:
        tentativa = int(input('Tente adivinhar o número pensado pela máquina (1 - 100): '))
        qtdTentativa += 1

        if tentativa != numeroGerado:
            print('Você errou, tente novamente...')
            continue
        else:
            print(f'\nParabéns! Você acertou em {qtdTentativa} tentativas')
            break
    
    print('-' * 19)

main()