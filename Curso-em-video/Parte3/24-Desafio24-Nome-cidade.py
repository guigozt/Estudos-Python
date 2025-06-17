def main():
    print('Digite o nome de uma cidade do Brasil: ', end='')
    nomeCidade = input().split()
    print(f'O nome da cidade começa com a palavra Santo?')
    print('SANTO' in nomeCidade[0].upper())

main()
