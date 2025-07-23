def notas(* nt, sit=False): #Recebe várias notas, para desempacotalas
    from statistics import mean

    if not nt:
        return {'ERRO: Nenhuma nota foi inserida!'}
    
    dicionario = {
        'Total': len(nt),
        'Maior': max(nt),
        'Menor': min(nt),
        'Média': round(mean(nt),2) #Arredonda, com 2 casas decimais
    }

    if sit:
        if dicionario['Média'] >= 7:
            dicionario['Situação'] = 'Excelente'
        elif dicionario['Média'] >= 5:
            dicionario['Situação'] = 'Razoável'
        else:
            dicionario['Situação'] = 'Ruim'

    return dicionario

def main():
    resp = notas(5.5, 5.5, 4, 6.5, sit=True)
    print(resp)
    print('-' * 70)
    resp = notas(5.5, 5.5, 4, 6.5, sit=False)
    print(resp)

main()