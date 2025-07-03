def main():
    boletim = []

    while True:
        nome = input('Nome do aluno(a): ')
        nota1 = float(input('Nota 1: '))
        nota2 = float(input('Nota 2: '))
        media = (nota1 + nota2) / 2 
        boletim.append([nome, [nota1, nota2], media])
#Indice                  0          1          2

        if input('Quer continuar? [S/N] ').strip().lower() != 's':
            break

    print(f'\n{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
    print('-' * 20)

    for posicao, aluno in enumerate(boletim):
        print(f'{posicao:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')

    while True:
        mostrarNotas = int(input('\nMostrar notas de qual aluno? (999 interrompe): '))

        if mostrarNotas == 999:
            print('Encerrando...')
            break
        elif 0 <= mostrarNotas < len(boletim): #Se mostrarNotas for maior ou igual a 0 (existir) e menor que a lista
            # Acessa o numero correspondente do aluno e o nome -> acessa a sublista "notas" inteira 
            print(f'As notas de {boletim[mostrarNotas][0]} são: {boletim[mostrarNotas][1]}')
        else:
            print('Número inválido!')
            
main()
