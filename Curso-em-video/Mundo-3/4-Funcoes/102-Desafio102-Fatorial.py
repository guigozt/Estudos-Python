def fatorial(num, show=False):
    fat = 1
    for i in range(num, 0, -1):
# ---------------------------------- Se show for true
        if show:
            print(i, end='')
            if i > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
# ------------------------------------ 
        fat *= i #Retorna no final (sozinho se show for False | após o processo se show for True )
    return fat

def main():
    print(fatorial(5, True))

main()