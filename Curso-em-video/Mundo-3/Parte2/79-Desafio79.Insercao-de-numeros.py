def main():
    lista = []

    for _ in range(5):
        numero = int(input('Digite um número: '))
        inserido = False #Controle para verificar se já foi inserido

        for posicao, valor in enumerate(lista): #A cada loop(principal) a posicao e valor voltam para o inicio: (posicao=0 e valor={numero inicial})
            if numero < valor:
                lista.insert(posicao, numero) #Insere o numero na posicao atual
                inserido = True
                break #Para, se nao fica inserindo ele na mesma posicao varias vezes

        if not inserido: #Se for False (é um número maior, então entra no final)
            lista.append(numero)

    print(f'A lista gerada tem os números: {lista}')

main()
