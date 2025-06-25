def main():
    frase = input('Digite uma frase qualquer: ').upper().strip()

    print(f'A letra [a] aparece {frase.count('A')} vezes')
    print(f'Ela aparece a primeira vez na posição: {frase.find('A')+1}')
    print(f'Ela aparece pela ultima vez na posição: {frase.rfind('A')+1}')

main()
