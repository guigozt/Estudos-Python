def main():
    n1, n2, n3 = map(int, input('Digite 3 números: ').split())
    
    print('== VERSÃO SIMPLES ==')
    print(f'{max(n1,n2,n3)} é o maior')
    print(f'{min(n1,n2,n3)} é o menor')
    print()
    print('== VERSÃO LÓGICA ==')

    #MAIOR
    if n1 >= n2 and n1 >= n3:
        maior = n1
    elif n2 >= n1 and n2 >= n3:
        maior = n2
    else:
        maior = n3

    #MENOR
    if n1 <= n2 and n1 <= n3:
        menor = n1
    elif n2 <= n1 and n2 <= n3:
        menor = n2
    else:
        menor = n3

    print(f'{maior} é o maior')
    print(f'{menor} é o menor')
        
main()
