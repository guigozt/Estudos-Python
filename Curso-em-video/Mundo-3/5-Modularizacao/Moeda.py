def formatacao(valorFuncao):
    return f'R$ {valorFuncao:.2f}'.replace('.',',')

def dobro(num, form=False):
    resultado = num * 2
    if form:
        return formatacao(resultado)
    else:
        return resultado

def metade(valor, form=False):
    resultado = valor / 2
    return formatacao(resultado) if form else resultado

def aumento(valor, porcentagem, form=False):
    resultado = valor + (valor * (porcentagem / 100))
    return formatacao(resultado) if form else resultado

def diminui(valor, porcentagem, form=False):
    resultado = valor - (valor * (porcentagem / 100))
    return formatacao(resultado) if form else resultado

def resumo(valor, aum, redu):
    print('-' * 30)
    print(f'{"RESUMO DO VALOR"}')
    print('-' * 30)

    print(f'Preço analisado:    {formatacao(valor)}')
    print(f'Dobro do preço:     {dobro(valor, True)}')
    print(f'Metade do preço:    {metade(valor, True)}')
    print(f'80% de aumento:     {aumento(valor, aum, True)}')
    print(f'35% de desconto:    {diminui(valor, redu, True)}')

    print('-' * 30)
    print()
