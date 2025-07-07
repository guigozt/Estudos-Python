#pessoas = dict() outra forma de criar dicionarios
pessoas = {'nome': 'Guilherme', 'sexo': 'M', 'idade': 21} #Uso mais comum de criar -> tupla "()" -> lista "[]" -> dicionario "{}"
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos de idade') #Usa "" para poder usar com fstring

#print(pessoas.keys()) -> Mostra "nome, sexo, idade"
#print(pessoas.values()) -> Mostra "guilherme, M, 21"
#print(pessoas.items()) -> Mostra todos os elementos

for chave, valor in pessoas.items(): #Pode acessar separadamente. Ex: for chave in pessoas.keys() ou for valor in pessoas.values()
    print(f'{chave} = {valor}')
    
del pessoas['sexo'] #Deletar a chave "sexo"
pessoas['nome'] = 'Leandro' #Modificar
pessoas['peso'] = 98.5 #Pra adicionar não é preciso de "append()"

print('-----------')

for chave, valor in pessoas.items():
    print(f'{chave} = {valor}')
    
print('----------')

estado1 = {'uf': 'Sao Paulo', 'sigla': 'SP'}
estado2 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
brasil = []
brasil.append(estado1) #Guarda os dois dicionarios em uma lista
brasil.append(estado2)
print(brasil)
print(brasil[0]['uf'])  #Acessa o indice 0 de brasil (primeiro dicionario) e a chave "uf"

print('---------')

estado = dict()
brasil2 = list()

for contEstado in range(3):
    estado['uf'] = input('Unidade Federativa: ') #Já cria uma chave
    estado['sigla'] = input('Sigla do Estado: ')
    brasil2.append(estado.copy()) #Forma de copiar os dados de um dicionario, usando o metodo copy() -> estado[:] não funciona
     
for est in brasil2: #Laço da lista
    for valor in est.values(): #Percorre o dicionario nesse for, nesse caso só peguei os valores
        print(f'{valor}', end=' ')
    print()