from datetime import date

def main():
    anoNascimento = int(input('Digite o ano de seu nascimento (AAAA): '))
    anoAtual = date.today().year
    idade = anoAtual - anoNascimento
    
    print()

    if idade <= 9:
        print('Você é um NINJA GENIN')
    elif idade <= 14:
        print('Você é um NINJA CHUNIN')
    elif idade <= 19:
        print('Você é um NINJA JOUNIN')
    else:
        print('Você é um NINJA KAGE')

main()