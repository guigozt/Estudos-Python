def main():
    aluno = {}
    
    aluno['nome'] = input('Nome: ')
    aluno['media'] = float(input(f'Media de {aluno["nome"]}: '))
    if aluno['media'] > 5:
        aluno['situacao'] = 'Aprovado(a)'
    else:
        aluno['situacao'] = 'Reprovado(a)'
    
    print('-' * 20)
    
    print(f'O aluno {aluno["nome"]} tem a média de {aluno["media"]:.2f}')
    print(f'Situação: {aluno["situacao"]}')
    
main()