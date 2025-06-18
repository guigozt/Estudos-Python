def mes(v):
    if v == 1:
        return 'January'
    elif v == 2:
        return 'February'
    elif v == 3:
        return 'March'
    elif v == 4:
        return 'April'
    elif v == 5:
        return 'May'
    elif v == 6:
        return 'June'
    elif v == 7:
        return 'July'
    elif v == 8:
        return 'August'
    elif v == 9:
        return 'September'
    elif v == 10:
        return 'October'
    elif v == 11:
        return 'November'
    else:
        return'December'

def main():
    valor = int(input('Digite o valor do mês correspondente: '))

    print(f'{mes(valor)}')

main()
