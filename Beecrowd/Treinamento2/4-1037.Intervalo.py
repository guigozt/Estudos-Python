def intervalo(v):
    if v >= 0 and v <= 25:
        return 'Intervalo [0,25]'
    elif v > 25 and v <= 50:
        return 'Intervalo (25,50]'
    elif v > 50 and v <= 75:
        return 'Intervalo (50,75]'
    elif v > 75 and v <= 100:
        return 'Intervalo (75,100]'
    else:
        return 'Fora do intervalo'
 
def main():
    valor = float(input('Digite o valor: '))

    print(intervalo(valor))

main()
