def main():
    lista = []

    for _ in range(5):
        numero = int(input('Digite um número: '))
        inserido = False #Controle para verificar se já foi inserido

        for posicao, valor in enumerate(lista): #A cada loop(principal) a posicao e valor voltam para o inicio: (posicao=0 e valor={numero inicial})
            if numero <= valor:
                lista.insert(posicao, numero) #Insere o numero na posicao atual
                inserido = True
                print(f'Adicionado na posição {posicao} da lista')
                break #Para, se nao fica inserindo ele na mesma posicao varias vezes

        if not inserido: #Caso seja a primeira interação ou numero seja maior que todos (ultimo)
            lista.append(numero)
            print('Adicionado no final da lista')

    print(f'A lista gerada tem os números: {lista}')

main()
