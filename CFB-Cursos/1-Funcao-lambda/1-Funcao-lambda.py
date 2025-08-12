def main():
    #lambda é uma função anonima
    # lambda 'argumentos' : 'retorno'
    r = lambda x, funcao: x + funcao(x)
    res = r(2, lambda x: x*x)   #x = 2, e funcao = uma outra função lambda
    print(f'Resultado do uso da função lambda: {res}')
    
main()