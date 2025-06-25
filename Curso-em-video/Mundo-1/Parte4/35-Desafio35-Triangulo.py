def main():
    a, b, c = map(float, input('Digite 3 valores: ').split())

    if a + b > c and b + c > a and c + a > b:
        print('Formam um Triangulo com sucesso!')
    else:
        print('Não com formam um Triangulo!')

main()
