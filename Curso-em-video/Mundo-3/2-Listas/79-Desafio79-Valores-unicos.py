def main():
    lista = []
    
    while True:
        valor = int(input('Digite um valor: '))

        if valor not in lista:
            lista.append(valor)
            print('[SUCESSO] Valor adicionado com sucesso...')
        else:
            print('[ERRO] Valor duplicado! Não vou adicionar...')

        op = input('Quer continuar? [S/N]:').strip().lower()

        if op != 's':
            print('\nEncerrando... vamos para a análise...')
            break
        
    lista.sort()
    print(f'\nA lista gerada tem os números: {lista}')

main()
