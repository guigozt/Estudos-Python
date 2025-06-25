def main():
    lanche = ('Hamburguer','Suco','Pizza','Pudim') #Tupla
    print(lanche[3])
    print(lanche[-2])
    print(lanche[1:3])
    print(lanche[2:])
    #lanche[1] = 'Refrigerante' -> Impossível
    for posicao, comida in enumerate(lanche): #Enumerate pega o indica e o valor
        print(f'Eu vou comer {comida} na posição {posicao}')

    print('\n------------\n')
    a = (2,5,4)
    b = (5,8,1,2)
    c = a + b
    print(c)
    print(c.count(2))
    print(c.index(5))

    print('\n------------\n')
    
    pessoa = ('Guilherme', 21, 'M', 99.88)
    print(pessoa)
    #del(pessoa[0]) -> Impossivel
    
main()
