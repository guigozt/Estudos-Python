import random

def menuJogo(jogadas):
    print('JOGO DO JOKENPO')
    print('-' * 15)
    print('[1]', jogadas[1])
    print('[2]', jogadas[2])
    print('[3]', jogadas[3])
    print('-' * 15)

def escolhaJogador(jogadas):
    while True:
        try:
            opcao = int(input('Escolha uma opção: '))
            jogadaEscolhida = jogadas[opcao]

            print('Você escolheu: ', jogadaEscolhida)
            return jogadaEscolhida
        except ValueError:
            print('[ERRO] Você precisa digitar um número (1, 2 ou 3)')
        except KeyError:
            print('[ERRO] Opção inválida, somente valores entre 1, 2 e 3')
        except KeyboardInterrupt:
            print('Jogo encerrado pelo usuário...')
            return None

def escolhaMaquina(jogadas):
    opcao = random.randint(1, 3)
    print('A Maquina escolheu:', jogadas[opcao])
    return jogadas[opcao]

def disputa(opJogador, opMaquina, jogadas):
    if opJogador == opMaquina:
        print('\nEMPATE ENTRE OS DOIS JOGADORES')
    elif(opJogador == jogadas[1] and opMaquina == jogadas[3]) or \
        (opJogador == jogadas[2] and opMaquina == jogadas[1]) or \
        (opJogador == jogadas[3] and opMaquina == jogadas[2]):
        print('\nO JOGADOR GANHOU COM ', opJogador.upper())
    else:
        print('\nA MAQUINA GANHOU COM', opMaquina.upper())

def menuControle():
    while True:
        try:
            opcao = input('\nQuer jogar novamente? (S/N): ').strip().lower()

            if opcao in ('s', 'n'):
                return opcao
            print('Opção inválida, tente novamente...')

        except KeyboardInterrupt:
            print('Jogo encerrado pelo usuário...')
            return 'n'

def main():
    jogadas = {
        1: 'Pedra',
        2: 'Papel',
        3: 'Tesoura'
    }

    while(True):
        menuJogo(jogadas)
        opcaoJogador = escolhaJogador(jogadas)
        opcaoMaquina = escolhaMaquina(jogadas)
        disputa(opcaoJogador, opcaoMaquina, jogadas)

        if menuControle() == 'n':
            print('Muito obrigado pela participação...')
            break

main()