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
    print('-' * 40)
    print(f'{"RESUMO DO VALOR":^40}')
    print('-' * 40)

    print(f'{"Preço analisado:":<25}{formatacao(valor):>15}')
    print(f'{"Dobro do preço:":<25}{dobro(valor, True):>15}')
    print(f'{"Metade do preço:":<25}{metade(valor, True):>15}')
    print(f'{f"{aum}% de aumento:":<25}{aumento(valor, aum, True):>15}')
    print(f'{f"{redu}% de desconto:":<25}{diminui(valor, redu, True):>15}')

    print('-' * 40)
    print()
