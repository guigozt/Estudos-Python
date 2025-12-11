def main():
    valor1 = int(input('Valor 1: '))
    valor2 = int(input('Valor 2: '))
    
    if valor1 > valor2:
        print(f'O valor {valor1} é maior que o valor {valor2}')
    elif valor2 > valor1:
        print(f'O valor {valor2} é maior que o valor {valor1}')
    else:
        print(f'O valor {valor1} é igual ao valor {valor2}')
        
main()