def main():
    jogador = {}
    gols = []
    
    jogador['Nome'] = input('Nome do jogador: ')
    jogador['Partidas'] = int(input(f'Quantas partidas {jogador["Nome"]} fez no campeonato? '))

    for partida in range(jogador['Partidas']):
        gols.append(int(input(f'    Quantos gols ele fez na {partida+1}ª partida? ')))
    
    jogador['Gols'] = gols
    jogador['Total'] = sum(gols)

    print('\nResultados do jogador ---------\n')

    for chave, valor in jogador.items():
        print(f'{chave} -> {valor}')

    print('-' * 20)

    print(f'O jogador {jogador["Nome"]} jogou {jogador["Partidas"]} partidas.')

    for i, v in enumerate(gols):
        print(f'    => Na partida {i+1}, fez {v} gols.')
        
    print(f'No total ele fez {jogador["Total"]} gols.')

main()