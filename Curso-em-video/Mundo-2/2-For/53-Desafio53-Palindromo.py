def ehPalindromo(fraseComp):
    tamanho = len(fraseComp)
    
    for i in range(tamanho // 2):
        if fraseComp[i] != fraseComp[(tamanho - 1) - i]:
            return False
    return True

def main():
    frase = input('Frase (Detector de Palindromo): ').lower().strip(' ')
    print('Frase original: ', frase)

    fraseCompleta = ''
    for i in frase:
        if i != ' ':
            fraseCompleta += i

    if ehPalindromo(fraseCompleta):
        print('É PALINDROMO!')
    else:
        print('NÃO É PALINDROMO...')

main()