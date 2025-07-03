def main():
    cadastro = []
    
# Guardar valores ---------------
    while True:
        nome = input('Nome: ')
        peso = float(input('Peso: '))
        cadastro.append([nome, peso]) #Adiciona uma sublista em cadastro, jeito correto
        opcao = input('Quer continuar? [S/N] ').strip().lower()
        if opcao != 's':
            break

    print(f'Ao todo, você cadastrou {len(cadastro)} pessoas')

# Maior e Menor Pesos ---------------------

    registroPesos = []
    for pessoa in cadastro:
        registroPesos.append(pessoa[1]) #Acessa o indice 1 (peso) e envia pra lista
        
    maiorPeso = max(registroPesos)
    menorPeso = min(registroPesos)
    print(f'O maior peso é {maiorPeso:.1f} kg. Peso de ', end='')

# Nome das Pessoas com os pesos correspondentes --------

    for pessoa in cadastro:
        if maiorPeso == pessoa[1]:
            print(f'[{pessoa[0]}] ', end='') #Acessa o indice 0 (nome) e junta
     
    print()

    print(f'O menor peso é {menorPeso:.1f} kg. Peso de ', end='')

    for pessoa in cadastro:
        if menorPeso == pessoa[1]:
            print(f'[{pessoa[0]}] ',end='')

main()
