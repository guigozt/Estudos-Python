def litros(t, c):
    return (t * c) / 12

def main():
    tempo = int(input())
    combustivel = int(input())
    print(f'{litros(tempo, combustivel):.3f}')

main()