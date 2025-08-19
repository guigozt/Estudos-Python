def main():
    casoTeste = int(input())
    qtdIn = 0
    qtdOut = 0
    
    for _ in range(casoTeste):
        valor = int(input())
        
        if 10 <= valor <= 20:
            qtdIn += 1
        else:
            qtdOut += 1
            
    print(f'{qtdIn} in')
    print(f'{qtdOut} out')
        
main()