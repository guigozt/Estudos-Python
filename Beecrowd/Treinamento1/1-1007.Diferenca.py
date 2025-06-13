def diferenca(a, b, c, d):
    return a * b - c * d

def main():
    num1 = int(input('Número 1: '))
    num2 = int(input('Número 2: '))
    num3 = int(input('Número 3: '))
    num4 = int(input('Número 4: '))

    print(f'DIFERENCA = {diferenca(num1, num2, num3, num4)}')

main()
