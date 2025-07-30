def media(n1, n2, n3):
    return (n1 * 2 + n2 * 3 + n3 * 5) / 10

def main():
    nota1 = float(input())
    nota2 = float(input())
    nota3 = float(input())

    print(f'MEDIA = {media(nota1, nota2, nota3):.1f}')

main()
