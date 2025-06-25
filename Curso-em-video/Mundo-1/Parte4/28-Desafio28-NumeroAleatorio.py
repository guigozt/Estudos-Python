from random import randint

def main():
    numAleatorio = randint(0,5)
    tentativa = int(input('Digite um número entre 0 a 5: '))

    if tentativa == numAleatorio:
        print(f'[CORRETO] você acertou o número gerado! -> [{numAleatorio}]')
    else:
        print(f'[ERRADO] Você não acertou o número gerado! -> [{numAleatorio}]')
    
main()

