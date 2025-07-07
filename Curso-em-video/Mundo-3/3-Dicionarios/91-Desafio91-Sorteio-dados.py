from random import randint
from time import sleep

def main():
    ranking = list() #Lista para guardar os dicionarios
    
    for i in range(1,5):
        jogador = { #Cria um dicionario a cada interação (4 jogadores)
            'nome' : f'Jogador {i}',
            'dado': randint(1,6)
        }
        print(f'{jogador["nome"]} tirou {jogador["dado"]}')
        ranking.append(jogador) #Envia para a lista
        sleep(0.8)
        
    print('\nRanking-------------\n')
    
    ranking.sort(key=lambda valor: valor['dado'], reverse=True) #Organiza com base no valor da chave "dado". Decrescente (reverse=true)
    
    for posicao, jogador in enumerate(ranking, 1): #Começa o for a partir do 1 (invés de fazer pontuação += 1)
        print(f'{posicao}º lugar: {jogador["nome"]} com {jogador["dado"]} pontos') #Posicao acessa os indices da lista / Jogador acessa os dicionarios (keys e values)
        sleep(0.8)
        
main()