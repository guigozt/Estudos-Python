def main():
    tripulacao = ('Luffy','Zoro','Nami','Sanji','Usopp','Chopper','Robin','Frank','Brook','Jimbe')
    
    for nome in tripulacao: #Percorre os "nomes" na tupla
        print(f'\nNa palavra {nome.upper()} temos as vogais: ', end='')
        
        for letra in nome: #Percorre cada letra em nome
            if letra.lower() in 'aeiou': #Se na letra tiver uma das vogais
                print(letra, end=' ')

main()
