def fichaJogador(nomeJ, qtdGols=0):
    print(f'O jogador {nomeJ} fez {qtdGols} gol(s) no campeonato!')

def main():
    nome = input('Nome do jogador: ').strip()
    gols = input('Quantidade de gols: ').strip()

    if gols.isnumeric(): #Se o input gols for um valor númerico, ele converte de string para int
        gols = int(gols)
    else: #Se nao atribui 0
        gols = 0

    if nome == '': #Caso o input seja vazio, atribui um valor para nome
        nome = '<desconhecido>'

    fichaJogador(nome, gols)
    print('-' * 20)
    
main()
