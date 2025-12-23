def calcularMedia(soma):
    return soma / 4

def main():
    somaIdades = 0
    quantidadeMulheres = 0
    maiorIdade = -1
    nomeMaisVelho = ''

    for i in range(4):
        nome = input(f'Nome da {i+1}ª pessoa: ').strip()
        idade = int(input(f'Idade da {i+1}ª pessoa: '))
        sexo = input(f'Sexo  da {i+1}ª pessoa (M/F): ').strip().upper()

        somaIdades += idade
        
        if sexo == 'F' and idade < 20:
            quantidadeMulheres += 1

        if sexo == 'M' and idade > maiorIdade:
            nomeMaisVelho = nome
            maiorIdade = idade
    
    print()
    print('ANALISE SOBRE O GRUPO')
    print('-' * 21)
    print(f'Média das idades: {calcularMedia(somaIdades):.2f}')
    print('Nome do homem mais velho: ', nomeMaisVelho)
    print('Quantidade de mulheres abaixo de 20 anos: ', quantidadeMulheres)

main()