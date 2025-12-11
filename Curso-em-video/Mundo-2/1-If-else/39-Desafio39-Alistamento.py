from datetime import date

def main():
    anoNascimento = int(input('Digite o ano de seu nascimento (AAAA): '))
    anoAtual = date.today().year
    idade = anoAtual - anoNascimento

    print(f'Sua idade: {idade}')

    if idade < 18:
        print('Ainda a tempo do seu Alistamento Militar')
    elif idade == 18:
        print('Está no tempo do seu Alistamento Militar')
    else:
        print('Já passou o tempo do seu Alistamento Militar')

main()