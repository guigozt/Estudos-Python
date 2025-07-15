from random import randint
from time import sleep
#from operator import itemgetter -> Serie a key para pegar o valor como base na hora de organizar -> Usaria o sorted(jogador.items(), key=itemgetter(1), reverse=True)

def main():
    ranking = list()   #Lista para guardar os dicionarios
    print('Valores sorteados:')

    for rodada in range(1, 5):
        jogador = { #Cria um dicionario a cada interação (4 jogadores)
            'nome': f'Jogador {rodada}',
            'dado': randint(1, 6)
        }

        print(f'O {jogador["nome"]} tirou {jogador['dado']}')
        ranking.append(jogador)
        sleep(0.8)

    print('\nRanking ---------\n')
    
    ranking.sort(key=lambda valor: valor['dado'], reverse=True) #Organiza com base no valor da chave "dado". Decrescente (reverse=true)

    for posicao, jogador in enumerate(ranking, 1):  #Começa o for a partir do 1 (invés de fazer pontuação += 1)
        print(f'{posicao} -> {jogador["nome"]} com {jogador["dado"]}')  #Posicao acessa os indices da lista / Jogador acessa os dicionarios (keys e values)
        sleep(0.8)

main()