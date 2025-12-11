def main():
    nota1, nota2 = map(float, input('Notas (1 e 2): ').split())
    media = (nota1 + nota2) / 2

    print(f'Nota 1: {nota1} \nNota 2: {nota2}')
    print(f'Média: {media:.1f}')

    if media < 5.0:
        print('\nREPROVADO')
    elif media < 7.0:
        print('\nRECUPERAÇÃO')
    else:
        print('\nAPROVADO')

main()