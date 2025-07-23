def leiaInt(mensagem):
    while True:
        valor = input(mensagem) #Input contem a mensagem na chamada do main, e valor recebe
        if valor.isnumeric(): #Verifica se o valor passado é um número. Ex: 123 -> True | '123' -> True | '123abc' -> False | -123 -> False 
            return valor
        else:
            print('\033[0;31m[ERRO] Digite um número inteiro válido\033[m')

def main():
    n = leiaInt('Digite um número: ')
    print(f'Você acabou de digitar o número: {n}')

main()