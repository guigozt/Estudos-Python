def main():
    nota1, nota2, nota3, nota4 = input('Informe as notas das 4 provas: ').split()
    nota1 = float(nota1)
    nota2 = float(nota2)
    nota3 = float(nota3)
    nota4 = float(nota4)

    media = (nota1*2 + nota2*3 + nota3*4 + nota4) / 10

    print(f'Media: {media:.1f}')

    if media >= 7.0:
        print('Aluno aprovado')
    elif media < 5.0:
        print('Aluno reprovado')
    else:
        print('Aluno em exame')

        notaExame = float(input('Informe a nota do exame: '))
        print(f'Nota do exame: {notaExame:.1f}')

        mediaExame = (media + notaExame) / 2

        if mediaExame >= 5.0:
            print('Aluno aprovado.')
            print(f'Media final: {mediaExame:.1f}')
        else:
            print('Aluno reprovado.')
            print(f'Media final: {mediaExame:.1f}')
            
main()
