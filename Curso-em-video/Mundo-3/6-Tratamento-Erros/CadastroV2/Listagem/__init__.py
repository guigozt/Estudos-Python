from CadastroV2 import Cores

def listar(arquivo):
    print('-' * 30)
    print(f'{Cores.cor('PESSOAS CADASTRADAS','negrito'):^30}')
    print('-' * 30)

    if not arquivo:
        print(f'{Cores.cor('Nenhuma pessoa cadastrada...', 'vermelho')}')
    else:
        for linha in arquivo:
            pessoa = linha.strip().split(';')
                    
            if len(pessoa) == 2:
                nome, idade = pessoa  
                print(f'{nome:<20}{idade:>5} anos')

