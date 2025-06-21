def primo(n): #Divisel apenas por 1 e por ele mesmo
    qtdDivisores = 0
    possivelDivisor = 1
    
    while possivelDivisor <= n:  #quando possivelDivisor chegar até o n (limite)
        if n % possivelDivisor == 0:
            qtdDivisores += 1
        possivelDivisor += 1

    if qtdDivisores == 2:
        return True

def main():
    qtdNumeros = int(input('Quantos números quer verificar? '))

    for contNumeros in range(qtdNumeros):
        numero = int(input('Número: '))

        if primo(numero):
            print(f'{numero} eh primo')
        else:
            print(f'{numero} nao eh primo')
            
main()
