def contarNotas(reais):
    nota100 = reais // 100
    resto = reais % 100
    print(f'{nota100} nota(s) de R$ 100,00')

    nota50 = resto // 50
    resto = resto % 50
    print(f'{nota50} nota(s) de R$ 50,00')

    nota20 = resto // 20
    resto = resto % 20
    print(f'{nota20} nota(s) de R$ 20,00')

    nota10 = resto // 10
    resto = resto % 10
    print(f'{nota10} nota(s) de R$ 10,00')

    nota5 = resto // 5
    resto = resto % 5
    print(f'{nota5} nota(s) de R$ 5,00')
        
    nota2 = resto // 2
    resto = resto % 2
    print(f'{nota2} nota(s) de R$ 2,00')

    nota1 = resto // 1
    resto = resto % 1
    print(f'{nota1} nota(s) de R$ 1,00')

def main():
    valor = int(input())

    print(f'{valor}')
    contarNotas(valor)
    
main()
