def main():
    primeiroTermo = int(input('Termo: '))
    razao = int(input('Razão: '))
    limite = 10

    for _ in range(limite):
        print(f'{primeiroTermo}', end=' -> ')
        primeiroTermo += razao
    
    print('Acabou...')
    
main()