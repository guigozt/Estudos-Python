from datetime import datetime

def main():
    pessoa = {
        'Nome': input('Nome: '),
        'Idade': int(input('Ano de nascimento: ')),
        'Carteira': int(input('Carteira de trabalho (0 não tem): '))
    }

    pessoa['Idade'] = datetime.now().year - pessoa['Idade'] #Date.now().year -> Pega o ano atual do sistema

    if pessoa['Carteira'] != 0:
        pessoa['AnoContratacao'] = int(input('Ano de contratação: '))
        pessoa['Salario'] = float(input('Salário (R$): '))
        pessoa['Aposentadoria'] = pessoa['Idade'] + ((pessoa['AnoContratacao'] + 35) - datetime.now().year)

    print('\nAnálise --------- \n')

    for chave, valor in pessoa.items():
        print(f'    => {chave} tem o valor de {valor}')

main()