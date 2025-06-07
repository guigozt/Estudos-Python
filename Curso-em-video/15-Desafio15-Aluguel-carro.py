kmPercorrido = float(input('Informa a quantidade de KM percorridos: '))
qtdDias = int(input('Informe a quantidade de dias alugados: '))

precoTotal = (qtdDias * 60) + (kmPercorrido * 0.15)

print(f'O total a pagar é de: R$ {precoTotal:.2f}')
