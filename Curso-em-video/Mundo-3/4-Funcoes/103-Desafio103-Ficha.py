def fichaJogador(nomeJ='<desconhecido>', qtdGols=0): #Atribui valores padrões caso não sejam passados
    print(f'O jogador {nomeJ} fez {qtdGols} gol(s) no campeonato!')

def main():
    nome = input('Nome do jogador: ').strip()
    gols = input('Quantidade de gols: ').strip()

    if gols.isdigit(): #Se o input gols for digitado, ele converte de string para int
        gols = int(gols)
    else: #Se nao atribui 0
        gols = 0

    if nome == '': #Caso o input seja vazio, atribui um valor para nome
        nome = '<desconhecido>'

    fichaJogador(nome, gols)
    print('-' * 20)
    
main()
