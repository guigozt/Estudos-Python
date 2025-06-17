def main():
    numero = int(input('Digite um número (0,9999): '))

    unidade = numero//1 % 10
    dezena = numero//10 % 10
    centena = numero//100 % 10
    milhar = numero//1000 % 10
    
    print(f'Milhar: {milhar}')
    print(f'Centena: {centena}')
    print(f'Dezena: {dezena}')
    print(f'Unidade: {unidade}') 

main()
 
