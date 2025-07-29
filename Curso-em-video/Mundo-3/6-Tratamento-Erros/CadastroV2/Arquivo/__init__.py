from CadastroV2 import Listagem, Cadastro, Cores, Erros

def arquivoExiste(nome):
    try: #Tenta verificar se o arquivo existe
        a = open(nome, 'rt') #Abre o arquivo em modo de leitura
        a.close() #Fecha o arquivo

    except FileNotFoundError:
        return False
    else:
        return True
    
def criarArquivo(nome):
    try:
        a = open(nome, 'wt+') #Abre um arquivo e já cria em modo de edição (escrita)
        a.close()
    except:
        print(f'{Cores.cor('Houve um erro na criação do arquivo', 'vermelho')}')
    else:
        print(f'{Cores.cor('Arquivo criado com sucesso', 'verde')}')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
        linhas = a.readlines()
    except:
        print(f'{Cores.cor('Erro ao ler arquivo!','vermelho')}')
    else:
        Listagem.listar(linhas) #Chama a função de listagem

def cadastrarArquivo(arquivo):
    try:
        Cadastro.cadastrar(arquivo) #Chama a função de cadastrar
    except:
        print(f'{Cores.cor('Erro em chamar o arquivo!','vermelho')}')
