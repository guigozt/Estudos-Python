def main():
    while True:
        try:
            inicial, final = map(int, input().split()) #Converte as strings e guarda numa "lista"
            numDiferentes = 0

            for numero in range(inicial, final+1):
                #set elimina duplicatas -> Ex: numero = '122' -> set('122') = {'1','2'}
                #Compara o tamanho de numero com o tamanho de set(numero) -> ex: '122' tem tamanho 3, e set('122') tem tamanho 2
                if len(str(numero)) == len(set(str(numero))):
                    numDiferentes += 1

            print(numDiferentes)
            
        except EOFError: #Fim de entrada, e para o programa
            break
    
main()
