from CadastroV2 import Menu, Arquivo, Encerramento, Cores

def main():
    arquivo = 'Desafio115.txt' #Recebe o nome do arquivo
    if not Arquivo.arquivoExiste(arquivo):
        Arquivo.criarArquivo(arquivo)
        
    while True:
        resposta = Menu.menu(['Listar pessoas', 'Cadastrar uma nova pessoa', 'Sair do sistema']) #Passa uma lista (as opções do menu) e retorna a opção escolhida
        #Dicionario que armazena os pacotes, uso do lambda para elas não serem executadas na hora
        acoes = {
            1: lambda: Arquivo.lerArquivo(arquivo),
            2: lambda: Arquivo.cadastrarArquivo(arquivo),
            3: lambda: Encerramento.sair()
        }

        if resposta in acoes: #Se a opção escolhida estiver no dicionario, ai sim chama a função correspondente
            acoes[resposta]()
            if resposta == 3:
                break
            input(f'{Cores.cor('\nPressione qualquer tecla para continuar...', 'azul')}')
        else:
            print(f'{Cores.cor('Opção inválida', 'vermelho')}')
main()