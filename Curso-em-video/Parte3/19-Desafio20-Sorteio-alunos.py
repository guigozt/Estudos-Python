def main():
    from random import random, choice
    print('Quem vai apagar a lousa? \n')
    aluno1 = input('Nome do primeiro aluno: ')
    aluno2 = input('Nome do segundo aluno: ')
    aluno3 = input('Nome do terceiro aluno: ')
    aluno4 = input('Nome do quarto alunio: ')
    
    alunos = [aluno1, aluno2, aluno3, aluno4]

    sorteado = random.choice(alunos)

    print(f'O escolhido é: {sorteado}') 

main()
