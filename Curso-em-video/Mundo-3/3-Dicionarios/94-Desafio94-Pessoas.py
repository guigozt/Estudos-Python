def main():
    pessoas = []
    while True:
        cadastro = {'Nome': input('Nome: ')} 

        while True:
            sexo = input('Sexo [M/F]: ').strip().upper()
            if sexo in 'MF':
                cadastro['Sexo'] = sexo
                break
            print('[ERRO] Por favor digite apenas M ou F!')
                    
        cadastro['Idade'] = int(input('Idade: '))
        pessoas.append(cadastro)

        while True:
            resposta = input('Quer continuar? [S/N]: ').strip().upper()
            if resposta in 'SN':
                break
            print('[ERRO] Responda apenas S ou N')

        if resposta == 'N':
            break

    print('\nAnálise --------- \n')
    print(f'=> O grupo tem {len(pessoas)} pessoa(s) cadastrada(s)')

    somaIdade = sum(p['Idade'] for p in pessoas)
    mediaIdade = somaIdade / len(pessoas)
    print(f'=> A média de idade do grupo é de: {mediaIdade:.2f} anos')

    mulheres = [p['Nome'] for p in pessoas if p['Sexo'] == 'F']
    print(f'=> As mulheres cadastradas foraGm: {", ".join(mulheres) if mulheres else "Nenhuma"}')

    print('\n=> Listas de pessoas que estão acima da média de idade do grupo:')
    for pessoa in pessoas:
        if pessoa['Idade'] > mediaIdade:
            print(f'Nome: {pessoa["Nome"]} | Sexo: {pessoa["Sexo"]} | Idade: {pessoa["Idade"]}')

    print('\n<< Encerrado >>')

main()