def mensagem(txt):
    tamanho = len(txt)
    print('=' * tamanho)
    print(txt.upper())
    print('=' * tamanho)

def main():
    texto = input('Escreva um texto qualquer: ')
    print()
    mensagem(texto)

main()