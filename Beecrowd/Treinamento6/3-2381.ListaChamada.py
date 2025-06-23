def main():
    qtdAlunos, sorteado = map(int, input().split())
    alunos = []

    for _ in range(qtdAlunos):
        alunos.append(input())
    alunos.sort()

    print(alunos[sorteado-1])

main()
