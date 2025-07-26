try: #Tenta fazer o bloco...
    a = int(input('Num1: '))
    b = int(input('Num2: '))
    res = a / b

except (ValueError, TypeError): #Pode tratar dois tipos de erros (Valor e Tipo)
    print('Tivemos um problema com os tipos de dados')
except ZeroDivisionError:
    print('Impossível divisão por 0')
except: #Caso der algum erro...
    print('Tivemos um problema!')
#except Exception as erro: #Pode criar uma variavel que armazena o tipo de erro, e imprime a classe do erro (Bom para desenvlvedores!)
#    print(f'Problema encontrado: {erro.__class__}')
else: #Se não (se deu certo)
    print(f'Resultado: {res}')
finally: #Finaliza, mesmo se der dado errado ou certo
    print('Volte sempre, muito obrigado!')