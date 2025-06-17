def main():
    nome = input('Digite o seu nome completo: ').strip()
    
    print(f'Seu nome em Maisculas:',nome.upper())
    print(f'Seu nome em Minusculas: ',nome.lower())
    print(f'Quandidade de letras:',len(nome) - nome.count(' '))
    
    nome = nome.split()
    print(f'Quantidade de letras do primeiro nome:', len(nome[0]))

main()
