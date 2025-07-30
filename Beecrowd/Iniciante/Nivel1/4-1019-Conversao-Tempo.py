def main():
    tempo = int(input())
    hora = tempo // 3600
    resto = tempo % 3600
    minutos = resto // 60
    segundos = resto % 60

    print(f'{hora}:{minutos}:{segundos}')

main()