def conversao(numero, base):
    if numero == 0:
        return 0
    
    digitos = '0123456789ABCDEF'
    resultado = ''

    while numero > 0:
        resto = numero % base
        resultado = digitos[resto] + resultado
        numero = numero // base

    return resultado

def main():
    valor = int(input('Digite um valor: '))
    print('\n=== OPÇÕES DE CONVERSÃO ===')
    print('[1] para Binario')
    print('[2] para Octal')
    print('[3] para Hexadecimal')
    opcao = int(input('Qual opção você quer?: '))

    if opcao == 1:
        print('Valor em Binário: ',conversao(valor, 2))
    elif opcao == 2:
        print('Valor em Octal: ',conversao(valor, 8))
    else:
        print('Valor em Hexadecimal: ',  conversao(valor, 16))

main()