num = (2,5,9,1)
print(f'Tupla: {num}')
#num[2] = 3

numero = [2,5,9,1]
numero.append(7)
numero.insert(2,2) #Insert: insere na lista (posicao, numero adicionado) a lista vai se atualizar
numero.sort(reverse=True) #Sort: Organiza a lista / Reverse=True: Inverte a lista
#Pop: remove o ultimo elemento da lista, mas pode ser pop(3)
numero.remove(2) #Remove: remove o primeiro que aparece
print(f'Lista: {numero}')
print(f'Essa lista tem {len(num)} elementos')

if 5 in numero:
    numero.remove(5)
    print('5 removido!')
    print(f'Lista: {numero}')
else:
    print('5 não encontrado!')

#---------------------------------
print('\nOutra lista...\n')

valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for cont in range(5):
    valores.append(input('Valor: '))

for p, v in enumerate(valores):
    print(f'Na posição [{p}] econtrei o valor: {v}')

print('Fim...')

#------------------------------------
print('\nOutra lista...\n')

a = [2,3,4,7]
b = a
b[2] = 5 #Se alterar o valor de B, muda-se tbm em A??
#b = a[:] -> Assim B recebe todos os valores de A
print(f'Lista A: {a}')
print(f'Lista B: {b}')
