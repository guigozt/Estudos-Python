def ehprimo(num):
    if num < 2:
        return False
    
    if num % 2 == 0:
        return num == 2

    for i in range(3, num, 2):
        if num % i == 0:
            return False
    return True

def main():
    numero = int(input('Número: '))

    if ehprimo(numero):
        print('É PRIMO')
    else:
        print('NÃO É PRIMO')

main()