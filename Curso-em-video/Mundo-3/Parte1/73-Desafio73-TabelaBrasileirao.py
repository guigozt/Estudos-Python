def main():
    tabela = ('Botafogo','Palmeiras','Flamengo', 'Fortaleza','Internacional', 'São Paulo', 'Corinthians', 'Bahia', 'Cruzeiro', 'Vasco', 'Vitoria', 'Atletico Mineiro', 'Fluminense', 'Gremio', 'Juventude', 'Red Bull Bragantino', 'Atletico Paranaense', 'Criciuma', 'Atletico Goianiense', 'Cuiaba')

    print(f'Lista de times do Brasileirão: \n{tabela}')
    print('='*20)
    
    primeirosTimes = tabela[:5]
    print(f'Os 5 primeiros times são: \n{primeirosTimes}')
    print('='*20)
    
    ultimosTimes = tabela[16:]
    print(f'Os 4 primeiros times são: \n{ultimosTimes}')
    print('='*20)
    
    tabelaA = sorted(tabela)
    print(f'Times em ordem Alfabetica: {tabelaA}')
    print('='*20)

    print(f'O Flumisense está na {tabela.index("Fluminense")+1}ª posição')

main()
