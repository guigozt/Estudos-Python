def leiaInt(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
        except:
            print('\033[31mERRO! Por favor digite um número inteiro válido\033[m')
        else:
            return valor
        
def leiaFloat(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
        except KeyboardInterrupt:
            print(('\033[34m\nO usuário preferiu não digitar esse número\033[m'))
            valor = 0
            return valor
        except:
            print('\033[34mERRO! Por favor digite um número inteiro válido\033[m')
        else:
            return valor

def main():
    numInt = leiaInt('Digite um número Inteiro: ')
    numFlot = leiaFloat('Digite um número Real: ')
    print(f'Número Inteiro: {numInt}')
    print(f'Número Real: {numFlot}')
main()