from Cadastro import Cores
erros = {
        ValueError: '[ERRO] Digite um número inteiro válido',
        KeyboardInterrupt: '[ERRO] Entrada cancelada pelo usuário',
        EOFError:'[ERRO] nEntrada finalizada abruptamente'
}

def cadastrar(cadastro):
    print('-' * 30)
    print(f'{Cores.cor('NOVO CADASTRO','negrito'):^30}')
    print('-' * 30)
    
    try:
        nome = input('Nome: ')
        idade = int(input('Idade: '))
    except(ValueError, KeyboardInterrupt, EOFError) as erro:
        tipoErro = type(erro)
        mensagemErro = erros.get(tipoErro, 'Erro desconhecido')
        print(f'{Cores.cor(mensagemErro, 'vermelho')}')
    else:
        try:
            pessoa = {'Nome': nome, 'Idade': idade}
            cadastro.append(pessoa)
        except:
            print('[ERRO] no cadastro!')
        else:
            print(f'Novo registro de {pessoa["Nome"]} adicionado')
