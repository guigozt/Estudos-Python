from CadastroV2 import Cores, Erros

def menu(opcoes):
    print('-' * 30)
    print(f'{Cores.cor('MENU PRINCIPAL','negrito'):^30}')
    print('-' * 30)
    indice = 1
    for item in opcoes:
        print(f'{Cores.cor(indice,'amarelo')} - {Cores.cor(item, 'azul')}')
        indice += 1
    print('-' * 30)

    try:
        opc = int(input(Cores.cor('Sua opção: ', 'amarelo')))

    except (ValueError, KeyboardInterrupt, EOFError) as erro: #Chama os possiveis erros de erro
        mensagemErro = Erros.erros.get(type(erro), 'Erro desconhecido') #Passa o tipo de erro (int) e a mensagem padrão
        print(Cores.cor(mensagemErro, 'vermelho'))
    else:
        return opc
