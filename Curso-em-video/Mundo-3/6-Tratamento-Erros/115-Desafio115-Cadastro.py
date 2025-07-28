from Cadastro import Cadastragem, Listagem, Encerramento, Menu, Cores #Importações de Pacotes
import os #Usado para verificar existencia de algum arquivo
arquivo = 'cadastro.txt' #Nome do arquivo que será gerado

#Define um dicionario para possiveis erros (mais pratico e sem repetção de código)
erros = {
        ValueError: '[ERRO] Digite um número inteiro válido',
        KeyboardInterrupt: '[ERRO] Entrada cancelada pelo usuário',
        EOFError:'[ERRO] nEntrada finalizada abruptamente'
}

def carregarCadastro():
    cadastro = []
    if os.path.exists(arquivo): #Verifica se o arquivo existe
        with open(arquivo, 'r', encoding='utf-8') as f: #Abre o arquivo em modo de leitura 'r' e chama de f
            for linha in f:
                partes = linha.strip().split(';') #Divide a linha no caractere ";" (nome;idade)
                if len(partes) == 2:
                    nome, idade = partes
                    cadastro.append({'Nome':nome, 'Idade':int(idade)}) #Joga o dicionario gerado para a lista
    return cadastro

def salvarCadastro(cadastro):
    with open(arquivo, 'w', encoding='utf-8') as f: #Abre o arquivo em modo de escrita 'w'
        for pessoa in cadastro:
            f.write(f'{pessoa["Nome"]};{pessoa["Idade"]}\n')

def main():
    cadastro = carregarCadastro() #Recebe a lista existente

    while True:
        Menu.menu()
        try:
            opcao = int(input(Cores.cor('Sua opção: ', 'amarelo')))

        except (ValueError, KeyboardInterrupt, EOFError) as erro: #Chama os possiveis erros de erro
            tipoErro = type(erro) #Recebe um valor int para o tipo de erro
            mensagemErro = erros.get(tipoErro, 'Erro desconhecido') #Recebe uma requisição no dicionario "erros", a mensagem padrão é "erro desconhecido"
            print(Cores.cor(mensagemErro, 'vermelho'))
        else:
            acoes = {
                1: lambda: Listagem.listar(cadastro), #Passa a lista cadastro como parametro, uso do lambda para guardar em acoes, impedindo que execute na hora
                2: lambda: Cadastragem.cadastrar(cadastro), 
                3: lambda: Encerramento.sair()
            }
            if opcao in acoes:
                acoes[opcao]() #Aqui sim executa a função
                if opcao in [2, 3]:
                    salvarCadastro(cadastro)
                if opcao == 3:
                    break
                input(Cores.cor('\nPressione ENTER para continuar...', 'azul'))
            else:
                print(Cores.cor('Opção inválida!', 'vermelho'))
main()