from time import sleep

def cor(texto, cor='verde'):
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

def encerraPrograma():
    print('=' * 36)
    print(cor('ENCERRANDO... OBRIGADO E VOLTE SEMPRE!', 'vermelho'))
    print('=' * 36)

def sistemaAjuda():
    print(cor('~' * 36, 'azul'))
    print(cor('SISTEMA DE AJUDA PYHELP'.center(36), 'negrito'))
    print(cor('~' * 36, 'azul'))

def sistemaHelp(comando):
    print(cor(f'Acessando o manual do comando "{comando}"...', 'amarelo'))
    sleep(1)
    print(cor('~' * 36, 'roxo'))
    help(comando)
    print(cor('~' * 36, 'roxo'))
    sleep(1)

def main():
    while True:
        sistemaAjuda()
        resposta = input(cor('Função ou Biblioteca ("fim" para encerrar) > ', 'ciano')).strip().lower()

        if resposta == 'fim':
            encerraPrograma()
            break
        elif resposta == '':
            print(cor('[ERRO] Nenhum comando digitado!', 'vermelho'))
            continue
        else:
            sistemaHelp(resposta)

main()