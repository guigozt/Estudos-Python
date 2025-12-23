from datetime import datetime
def main():
    quantidadeMaiores = 0
    quantidadeMenores = 0

    for i in range(7):
        anoNascimento = int(input(f'Digite o Ano de Nascimento da {i+1}ª pessoa: '))
        anoAtual = datetime.now().year
        idade = anoAtual - anoNascimento

        if idade >= 18:
            quantidadeMaiores += 1
        else:
            quantidadeMenores += 1
    
    print()
    print(f'A quantidade de pessoas que já atingiram a maioridade é de: {quantidadeMaiores} pessoas')
    print(f'A quantidade de pessoas que ainda não atingiram a maioridade é de: {quantidadeMenores} pessoas') 

main()