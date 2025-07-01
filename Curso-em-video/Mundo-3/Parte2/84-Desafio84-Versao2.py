def main():
    cadastro = []
    
    while True:
        nome = input('Nome: ')
        peso = float(input('Peso: '))
        cadastro.append([nome, peso])
        if input('Quer continuar? [S/N] ').strip().lower() != 's':
            break

    print(f'\nAo todo, você cadastrou {len(cadastro)} pessoas')

    maiorPeso = max(cadastro, key=lambda pessoa: pessoa[1])[1]
    menorPeso = min(cadastro, key=lambda pessoa: pessoa[1])[1]
    #lambda cria um nome pra key, que pega o indice[1] e retorna [1] = peso

    print(f'O maior peso é {maiorPeso:.1f} kg. Peso de ', end='')
    print(', '.join([pessoa[0] for pessoa in cadastro if pessoa[1] == maiorPeso]))
    #Junta com join a lista comprimida, que pega o nome de cada pessoa em cadastro e já compara o peso

    print(f'O menor peso é {menorPeso:.1f} kg. Peso de ', end='')
    print(','.join([pessoa[0] for pessoa in cadastro if pessoa[1] == menorPeso]))

main()
