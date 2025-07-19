def titulo(txt): #Passa o parametro que vai atualizar de acordo com o programa principal
    print('-' * 30)
    print(txt)
    print('-' * 30)

def soma(a,b):
    print (f'A soma de {a + b}')

def contador(* num): #Recebe vários valores, vão ser jogados em uma tupla 
    tamanho = len(num)
    print(f'Recebi os valores {num} e são ao todo: {tamanho} números')

def dobraValores(lista):
    i = 0
    while i < len(lista):
        lista[i] *= 2
        i+= 1

def main():
#---------------------------------
    titulo('  CURSO EM VIDEO  ')
#---------------------------------
    soma(4,5)
    soma(8,9)

    print()
#---------------------------------
    contador(2,1,7)
    contador(8, 0)
    contador(4,4,7,6,2)
    print()

#---------------------------------
    valores = [6,2,8,9,2]
    print(valores)
    dobraValores(valores)
    print(f'Valores dobrados: {valores}')

main()