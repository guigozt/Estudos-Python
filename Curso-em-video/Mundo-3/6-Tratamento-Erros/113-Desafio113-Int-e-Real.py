def leiaInt(mensagem):
    while True:
        try:
            valor = int(input(mensagem))

        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor digite um número inteiro válido\033[m')
            continue #Volta pro começo do laço
        except(KeyboardInterrupt):
            print('\033[31m\nEntrada de dados foi interrompida pelo usuário!\033[m')
            return 0
        else:
            return valor
        
def leiaFloat(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor digite um número inteiro válido\033[m')
            continue 
        except(KeyboardInterrupt):
            print('\033[31m\nEntrada de dados foi interrompida pelo usuário!\033[m')
            return 0
        else:
            return valor

def main():
    numInt = leiaInt('Digite um número Inteiro: ')
    numFlot = leiaFloat('Digite um número Real: ')
    print(f'Número Inteiro: {numInt}')
    print(f'Número Real: {numFlot}')
main()