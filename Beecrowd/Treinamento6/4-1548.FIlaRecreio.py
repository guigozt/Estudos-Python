def quantos_nao_mudaram(alunos):
    #sorted cria outra lista ordenada
    #sort ordena a propria lista
    #reverse=True -> lista é invertida (descrescente no caso)
    copiaLista = sorted(alunos, reverse=True)
    qtd = 0
    
    for i in range(len(alunos)):
        if alunos[i] == copiaLista[i]: #Compara as posições das duas listas
            qtd += 1
    return qtd

def main():
    filas = int(input())

    for _ in range(filas):
        qtdAlunos = int(input())
        alunos = list(map(int, input().split())) #usa o list para jogar todos os split na lista
        print(quantos_nao_mudaram(alunos))
main()
