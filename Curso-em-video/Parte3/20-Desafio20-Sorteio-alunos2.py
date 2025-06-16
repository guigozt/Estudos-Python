def main():
    from random import sample
    print('Qual vai ser a ordem de apresentação? \n')
    aluno1 = input('Nome do primeiro aluno: ')
    aluno2 = input('Nome do segundo aluno: ')
    aluno3 = input('Nome do terceiro aluno: ')
    aluno4 = input('Nome do quarto alunio: ')
    
    alunos = [aluno1, aluno2, aluno3, aluno4]

    ordem = sample(alunos, 4)

    print(f'A ordem de apresentação é: {ordem}')
    

main()
