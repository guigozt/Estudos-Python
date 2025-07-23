from time import sleep

def cor(texto, cor='verde'): #Definição de cores, padrão da cor é verde
    cores={
        'vermelho': '\033[31m',
        'verde': '\033[32m',
        'amarelo': '\033[33m',
        'azul': '\033[34m',
        'roxo': '\033[35m',
        'ciano': '\033[36m',
        'negrito': '\033[1m',
        'reset': '\033[m'
    }
    return f'{cores.get(cor, '')}{texto}{cores['reset']}'

#--------------------------------------------------------------------------
def encerraPrograma():
    print(cor('=' * 36, 'vermelho'))
    print(cor('ENCERRANDO... OBRIGADO E VOLTE SEMPRE!', 'vermelho'))
    print(cor('=' * 36, 'vermelho'))

#--------------------------------------------------------------------------
def sistemaAjuda():
    print(cor('~' * 36, 'azul'))
    print(cor('SISTEMA DE AJUDA PYHELP'.center(36), 'negrito'))
    print(cor('~' * 36, 'azul'))

# -------------------------------------------------------------------------
def sistemaHelp(comando):
    print(cor(f'Acessando o manual do comando "{comando}"...', 'amarelo'))
    sleep(1)
    print(cor('~' * 36, 'roxo'))
    help(comando)
    print(cor('~' * 36, 'roxo'))
    sleep(1)

def main():
    while True:
        sistemaAjuda() #Titulo do programa
        resposta = input(cor('Função ou Biblioteca ("fim" para encerrar) > ', 'ciano')).strip().lower()

        if resposta == 'fim':
            encerraPrograma() #Mensagem de encerramento
            break
        elif resposta == '': #Se o input for vazio
            print(cor('[ERRO] Nenhum comando digitado!', 'vermelho'))
            continue #O programa retorna lá pro while
        else:
            sistemaHelp(resposta) #Chama a função de help

main()