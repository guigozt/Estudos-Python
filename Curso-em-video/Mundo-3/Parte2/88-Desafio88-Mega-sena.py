from random import sample
from time import sleep 

def main():
    mega = []
    qtdJogos = int(input('Quantos jogos você quer que eu sorteie? '))

    for _ in range(qtdJogos):
        #Gera 6 números unicos entre 1 e 60
        sorteio = sample(range(1, 61), 6) #Vai ser gerada uma "linha" já com os valores aleatórios
        sorteio.sort()
        mega.append(sorteio) #Cada lista de "linha" vai ser enviada para mega

    print(f'\n------ SORTEANDO {qtdJogos} JOGOS ------\n')

    for posicao, numero in enumerate(mega):
        print(f'Jogo {posicao+1}: {numero}') #Acessa mega[0], mega[1]...
        sleep(0.8) #Tempo para imprimir

    print('\n--------- BOA SORTE ---------')
    
main()
