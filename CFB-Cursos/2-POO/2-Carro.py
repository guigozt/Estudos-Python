def main():
    class Carro():
        nome = ''
        velocidadeMaxima = 0
        cor = ''
        ligado = False

        def __init__(self, nm, velMax, co, lig):    
            #Construtor, função que já inicia com a classe (__init__)
            #self é para referenciar os atributos da própria classe -> this
            self.nome = nm
            self.velocidadeMaxima = velMax
            self.cor = co
            self.ligado = lig

        def mostrar(self):
            print(f'Nome.............: {self.nome}')
            print(f'Velocidade Máxima: {self.velocidadeMaxima}')
            print(f'Cor..............: {self.cor}')

            estado = 'Sim' if self.ligado else 'Não'
            print(f'Estado...........: {estado}') 

        def ligar(self):
            self.ligado = True
            print('Ligando...')
        
        def desligar(self):
            self.ligado = False
            print('Desligando...')

        def acelerar(self):
            if self.ligado:
                print(f'\nCarro {self.nome} está andando!')
            else:
                print(f'\nCarro {self.nome} está parado!')

    carro1 = Carro('Fox', 100, 'Preto', False)
    carro2 = Carro('Corola', 200, 'Azul', False)

    carro1.mostrar()
    carro1.ligar()
    carro1.acelerar()

    print('-' * 30)

    carro2.mostrar()
    carro2.acelerar()

main()