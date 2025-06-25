from random import sample #Sample gera números unicos

def main():
    numAleatorios = tuple(sample(range(0, 100), 5)) #5 valores unicos de 0 a 5
    print(f'Os valores sorteados foram: {numAleatorios}')

    print('\nUsando MAX e MIN')
    print(f'O maior valor sorteado foi: {max(numAleatorios)}')
    print(f'O menor valor sorteado foi: {min(numAleatorios)}')

    print('\nUsando Lógica de verificação')
    maior = menor = numAleatorios[0]

    for numero in numAleatorios:
        if numero > maior:
            maior = numero

        if numero < menor:
            menor = numero

    print(f'O maior valor sorteado foi: {maior}')
    print(f'O menor valor sorteado foi: {menor}')
       
main()
