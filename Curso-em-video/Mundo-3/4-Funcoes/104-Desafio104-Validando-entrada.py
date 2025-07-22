def leiaInt(mensagem):
    while True:
        valor = input(mensagem).strip() #Input contem a mensagem na chamada do main, e valor recebe
        if valor.isdigit(): #Verifica se o valor passado é um número. Ex: 123 -> True | '123' -> True | '123abc' -> False | -123 -> False 
            return valor
        else:
            print('[ERRO] Digite um número inteiro válido')

def main():
    n = leiaInt('Digite um número: ')
    print(f'Você acabou de digitar o número: {n}')

main()