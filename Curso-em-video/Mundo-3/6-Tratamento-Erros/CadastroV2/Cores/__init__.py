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