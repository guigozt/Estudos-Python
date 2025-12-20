def main():
    frase = input('Frase (Detector de Palindromo): ').strip(' ')
    print('Frase original: ', frase)

    fraseCompleta = ''    
    for palavra in frase:
        if palavra != ' ':
            fraseCompleta += palavra

    tamanho = len(fraseCompleta)
    ehpalindromo = True

    for i in range(tamanho // 2):
        if fraseCompleta[i] != fraseCompleta[(tamanho - 1) - i]:
            ehpalindromo = False
            break
    
    if ehpalindromo:
        print('É PALINDROMO')
    else:
        print('NÃO É PALINDROMO...')

main()