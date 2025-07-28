from Cadastro import Cores

def menu():
    print('-' * 30)
    print(f'{Cores.cor('MENU PRINCIPAL','negrito'):^30}')
    print('-' * 30)
    print(f'{Cores.cor('1', 'amarelo')} - {Cores.cor('Ver pessoas cadastradas','azul')}')
    print(f'{Cores.cor('2','amarelo')} - {Cores.cor('Cadastrar uma nova pessoa','azul')}')
    print(f'{Cores.cor('3', 'amarelo')} - {Cores.cor('Sair do sistema','azul')}')
    print('-' * 30)
