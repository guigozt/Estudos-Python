def main():
    termo = int(input('Quantos termos quer mostrar?: '))
    
    primeiro = 0
    segundo = 1

    contador = 0

    print('SEQUÊNCIA FIBONACCI')
    print('-' * 19)

    while contador < termo:
        print(primeiro, end=' ')

        atual = primeiro + segundo
        primeiro = segundo
        segundo = atual

        contador += 1
    
main()