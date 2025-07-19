from random import randint

def maior(* valor): #Desempacota os valores
    print(f'Foram gerados {len(valor)} números')
    print(f'Valores: {valor}')
    print(f'O maior valor entre eles é: {max(valor)}')


def main():
    quantidade = randint(1, 10) #Quantidade de vezes que vai gerar numeros. ex: 5 vezes
    numeros = [randint(1, 100) for _ in range(quantidade)] #Gera uma lista, que vai fazer o loop "quantidade" vezes. E vai gerar um numero aleatório a cada loop -> outra forma: numero = randint(1,100) -> numeros.append(numero)

    maior(* numeros) #Desempacota os valores dentro de numeros. Ex: [1,2,3] -> 1, 2, 3 (separados)

main()