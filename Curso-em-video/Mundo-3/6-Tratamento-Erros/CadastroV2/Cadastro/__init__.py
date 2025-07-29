from CadastroV2 import Cores, Erros

def cadastrar(arquivo):
    print('-' * 30)
    print(f'{Cores.cor('NOVO CADASTRO','negrito'):^30}')
    print('-' * 30)
    
    try:
        nome = input('Nome: ')
        idade = int(input('Idade: '))

    except(ValueError, KeyboardInterrupt, EOFError) as erro:
        mensagemErro = Erros.erros.get(type(erro), 'Erro desconhecido')
        print(f'{Cores.cor(mensagemErro, 'vermelho')}')
    try:
        a = open(arquivo, 'at') #Abre o arquivo em modo de append (inserção)
    except:
        print(f'{Cores.cor('Houve um erro na abertura do arquivo!', 'vermelho')}')
    else:
        try:
            a.write(f'{nome};{idade}\n') #Escreve no arquivo as informações passadas
        except:
            print(f'{Cores.cor('Houve um erro na hora de escrever os dados','vermelho')}')
        else:
            print(f'{Cores.cor(f'Novo registro de {nome} adicionado','verde')}')
            a.close()
