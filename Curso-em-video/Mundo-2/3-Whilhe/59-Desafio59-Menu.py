def lerValores():
    return map(float, input('Digite dois numeros: ').split())

def menuOpcao():
    print('\nMENU DE OPÇÕES')
    print('-' * 14)

    print('[1] Somar')
    print('[2] Multiplicar')
    print('[3] Maior')
    print('[4] Digitar novos números')
    print('[5] Encerrar')

def somar(n1, n2):
    print(f'A soma entre os números {n1} + {n2} = {n1 + n2}')


def multiplicar(n1, n2):
    print(f'A multiplicação entre os números {n1} X {n2} = {n1 * n2}')

def maior(n1, n2):
    print(f'O maior valor entre os números {n1} e {n2} é: {max(n1, n2)}')


def main():
    num1, num2 = lerValores()
    
    while True:
        menuOpcao()

        while True:
            opcao = input('Escolha uma opção: ').strip()

            if opcao in '12345':
                opcao = int(opcao)
                break
            print('Opção inválida, tente novamente...')

        if opcao == 1:
            somar(num1, num2)
        elif opcao == 2:
            multiplicar(num1, num2)
        elif opcao == 3:
            maior(num1, num2)

        elif opcao == 4:
            num1, num2 = lerValores()
            continue
        else:
            print('\nObrigado por utilizar o programa')
            print('Saindo...')
            break 

main()