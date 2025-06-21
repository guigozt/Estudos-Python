def main():
    alunosSala = int(input('Quantos alunos tem na sala? '))
    epr, ehd, intrusos = 0, 0 , 0

    for contAlunos in range(alunosSala):
        matricula, sigla = input('Digite a matricula e a sigla do curso: ').split()

        if sigla == 'EPR':
            epr += 1
        elif sigla == 'EHD':
            ehd += 1
        else:
            intrusos += 1

    print(f'EPR: {epr}')
    print(f'EHD: {ehd}')
    print(f'INTRUSOS: {intrusos}')

main()
