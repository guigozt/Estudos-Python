from datetime import datetime

def voto(id):
    print(f'Com {id} anos: ', end='')

    if id >= 65:
        print('VOTO OPCIONAL')
    elif id >= 18:
        print('VOTO OBRIGATÓRIO')
    else:
        print('NÃO VOTA')

def main():
    nascimento = int(input('Informe qual o ano de seu nascimento(AAAA): '))
    idade = datetime.now().year - nascimento
    voto(idade)

main()