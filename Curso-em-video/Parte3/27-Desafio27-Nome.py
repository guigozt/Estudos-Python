def main():
    nome = input('Digite o seu nome completo: ').strip()
    n = nome.split()
    print(f'Seu primeiro nome é: {n[0]}')
    print(f'Seu ultimo nome é: {n[len(n)-1]}')
    
main()
