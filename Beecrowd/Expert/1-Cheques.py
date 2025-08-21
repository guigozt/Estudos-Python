def formata_moeda(reais, centavos):
    pass
 
def extenso_para_numerico(v):
    pass
 
def entrada():
    v = input().lower().removesuffix('.')
    v = v.replace('de reais', '?')
    v = v.replace('reais', '?')
    v = v.replace('real', '?')
    v = v.replace('centavos', '!')
    v = v.replace('centavo', '!')

    reais, centavos = '', ''

    if '?' in v and '!':
        reais, centavos = v.split('?')
    elif '?' in v:
        reais = v.removeprefix(' ?')
        reais = reais.rstrip()
    elif '!' in v:
        centavos = centavos.removeprefix(' e ').removesuffix(' !')

    return reais, centavos

def main():
    total_reais = 0
    total_centavos = 0

    while True:
        try:
            reais, centavos = entrada()

            print(f'reais = {reais}')
            print(f'centavos = {centavos}')
            #total_reais += extenso_para_numerico(reais)
            #total_centavos += extenso_para_numerico(centavos)

        except (EOFError, KeyboardInterrupt):
            break
 
main()