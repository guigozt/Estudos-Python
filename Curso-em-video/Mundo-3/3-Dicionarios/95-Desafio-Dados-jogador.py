def main():
    jogadores = []

    while True:
        jogador = dict() #A cada loop os dicionarios e listas são zerados
        gols = []
        jogador['Nome'] = input('Nome do jogador: ')
        jogador['Posicao'] = input('Posição: ')
        jogador['Camisa'] = int(input('Número da camisa: '))
        jogador['Partidas'] = int(input(f'Quantas partidas {jogador["Nome"]} fez no campeonato? '))

        for i in range(jogador['Partidas']):
            gols.append(int(input(f'    Quantos gols na {i+1}ª partida? ')))
        
        jogador['Gols'] = gols[:]
        jogador['Total'] = sum(gols)
        
        jogadores.append(jogador.copy()) #Joga cada dicionario na lista

        while True:
            resposta = input('Quer continuar? [S/N]: ').strip().upper()[0]
            if resposta in 'SN':
                break
            print('[ERRO] Responda apenas S ou N')

        if resposta == 'N':
            break

    print('\nAnálise do time ----------------- \n')
        
    print(f'{"Cod":<3} {"Nome":<20}{"Gols":<20}{"Total":<10}')
    print('-' * 50)

    for i, jogador in enumerate(jogadores):
        print(f'{i:<3} {jogador["Nome"]:<20}{str(jogador["Gols"]):<20}{jogador["Total"]:<10}')

    print('-' * 50)

    while True:
        busca = int(input('Mostrar dado de qual jogador? (999 para): '))
        if busca == 999:
            break

        if busca >= len(jogadores):
            print(f'[ERRO] Jogador não encontrado!')
        else:
            print(f'--- LEVANTAMENTO DO JOGADOR {jogadores[busca]["Nome"]}')

            for partida, gols in enumerate(jogadores[busca]['Gols']):
                print(f' => Na {partida+1}ª partida, fez {gols} gols')
            
        print('-' * 35)

main()