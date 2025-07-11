def main():
    aluno = {}

    aluno['nome'] = input('Nome do aluno: ')
    aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
    if aluno['media'] > 5:
        aluno['situacao'] = 'Aprovado'
    else:
        aluno['situacao'] = 'Reprovado'

    print('-' * 20)

    print(f'O aluno {aluno["nome"]} tem a média de {aluno["media"]}')
    print(f'Situação: {aluno["situacao"]}')

main()