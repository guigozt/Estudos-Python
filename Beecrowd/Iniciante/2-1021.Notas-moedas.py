def contarNotas(reais):
    nota100 = int(reais // 100)
    resto = int(reais % 100)
    print(f'{nota100} nota(s) de R$ 100.00')

    nota50 = int(resto // 50)
    resto = int(resto % 50)
    print(f'{nota50} nota(s) de R$ 50.00')

    nota20 = int(resto // 20)
    resto = int(resto % 20)
    print(f'{nota20} nota(s) de R$ 20.00')

    nota10 = int(resto // 10)
    resto = int(resto % 10)
    print(f'{nota10} nota(s) de R$ 10.00')

    nota5 = int(resto // 5)
    resto = int(resto % 5)
    print(f'{nota5} nota(s) de R$ 5.00')
        
    nota2 = int(resto // 2)
    resto = int(resto % 2)
    print(f'{nota2} nota(s) de R$ 2.00')

    return resto #Caso sobre 1 real. Ex: reais = 3

def contarMoedas(moeda1, centavos):

    print(f'{moeda1} moeda(s) de R$ 1.00') #O valor pode ser 0 (caso nao tenha havido sobra)

    moeda50 = centavos // 50
    sobra = centavos % 50
    print(f'{moeda50} moeda(s) de R$ 0.50')

    moeda25 = sobra // 25
    sobra = sobra % 25
    print(f'{moeda25} moeda(s) de R$ 0.25')

    moeda10 = sobra // 10
    sobra = sobra % 10
    print(f'{moeda10} moeda(s) de R$ 0.10')

    moeda05 = sobra // 5
    sobra = sobra% 5
    print(f'{moeda05} moeda(s) de R$ 0.05')

    moeda01= sobra // 1
    sobra = sobra % 1
    print(f'{moeda01} moeda(s) de R$ 0.01')

def main():
    valor = float(input()) #Ex: 5.73
    totalCentavos = round(valor * 100) #Tranforma tudo em centavo. Ex: 573
    #Round arredonda os números float
    reais = totalCentavos // 100 #Pega o 5
    centavos = totalCentavos % 100 #Pega o 73

    print('NOTAS:')
    sobra = contarNotas(reais)

    print('MOEDAS:')
    contarMoedas(sobra, centavos)
    

main()
