def main():
    numero = int(input('Número: '))
    quantDivisores = 0

    for i in range(1, numero+1):
        if numero % i == 0:
            quantDivisores += 1
    
    if quantDivisores == 2:
        print('O número',numero,'é primo!')
    else:
        print('O número',numero,'não é primo!')

main()