def main():
    termo = int(input('Número da Sequência: '))

    primeiro = 0
    segundo = 1
    cont = 0

    print('SEQUÊNCIA FIBONACCI')
    print('-' * 19)

    while cont < termo:
        print(primeiro, end=' ')

        atual = primeiro + segundo
        primeiro = segundo
        segundo = atual

        cont += 1
    
main()    