def multiplos(a, b):
    if b%a == 0 or a%b == 0:
        print ('São Multiplos')
    else:
        print ('Não são Multiplos')

def main():
    a, b = input('Digite os valores de A e B: ').split()
    a = int(a)
    b = int(b)

    multiplos(a, b)
    
main()
