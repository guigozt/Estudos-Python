def main():
    casos = int(input('Quantos números quer verificar? '))
    lista = []
    
    for _ in range(casos):
        numero = int(input('Número: '))
        soma = 0

        for contNumero in range(1, numero):
            if numero % contNumero == 0:
                soma += contNumero

        if soma == numero:
            lista.append(f'{numero} eh perfeito')
        else:
            lista.append(f'{numero} nao eh perfeito')

    for imprime in lista:
        print(imprime)
            
main()
