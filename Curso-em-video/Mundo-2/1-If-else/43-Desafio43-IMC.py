from math import pow

def calcularIMC(alt, peso):
    return peso / pow(alt, 2)

def resultadoIMC(imc):
    print(f'IMC: {imc:.2f}')

    if imc < 18.5:
        print('Você está abaixo do peso!')
    elif imc <= 25:
        print('Você está no peso ideal!')
    elif imc <= 30:
        print('Você está no sobrepeso!')
    elif imc <= 40:
        print('Você está obeso!')
    else:
        print('Você está em obesidade morbida!')

def main():
    altura = float(input('Digite sua altura: '))
    peso = float(input('Digite seu peso: '))

    imc = calcularIMC(altura, peso)
    resultadoIMC(imc)

main()