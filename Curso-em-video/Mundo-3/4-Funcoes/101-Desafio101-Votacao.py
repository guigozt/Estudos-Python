def voto(ano):
    from datetime import datetime
    idade = datetime.now().year - ano

    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'

def main():
    anoNascimento = int(input('Informe o seu ano de nascimento: '))
    print(voto(anoNascimento))

main()