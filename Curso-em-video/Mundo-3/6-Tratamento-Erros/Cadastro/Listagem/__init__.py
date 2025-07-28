from Cadastro import Cores

def listar(cadastro):
    print('-' * 30)
    print(f'{Cores.cor('PESSOAS CADASTRADAS','negrito'):^30}')
    print('-' * 30)

    if not cadastro:
        print('Nenhum cadastro encontrado...')
    else:
        for pessoa in cadastro:
            print(f'{pessoa["Nome"]:<20} {pessoa["Idade"]:>5} anos')
