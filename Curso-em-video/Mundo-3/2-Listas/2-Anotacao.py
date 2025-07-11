teste = list()
teste.append('Guilherme')
teste.append(40)
#-----------------------
galera = list()
galera.append(teste[:]) #galera recebe tudo de lista (copia)
#Muda os dados em teste
teste[0] = 'Maria' 
teste[1] = 22
#Depois galera adiciona os novos valores pra si
galera.append(teste[:])

print('Teste: ',teste)
print('Galera: ',galera)

#-----------------------
#             0     1      0    1     0       1
pessoas = [['Joao', 19],['Ana',33],['Joaquim',14]]
#               0           1            2  
print('Pessoas',pessoas)
print('Pessoas[nome]',pessoas[0][0]) #Joao
print('Pessoas[idade]',pessoas[0][1]) #19

for pessoa in pessoas:
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade')

galera2 = []
dado = list()
totmaior, totmenor = 0, 0
for c in range(0,3):
    dado.append(input('Nome: '))
    dado.append(int(input('Idade: ')
                    ))
    galera2.append(dado[:])
    dado.clear()

for p in galera2:
    if p[1] >= 18:
        print(f'{p[0]} é de maior')
        totmaior += 1
    else:
        print(f'{p[0]} é de menor')
        totmenor += 1
        
print(f'Temos {totmaior} maiores e {totmenor} menores de idades')
