def main():
    exp = input('Digite uma expressão: ')
    pilha = list() #Armazena os parenteses

    for simbolo in exp:
        if simbolo == '(':
            pilha.append('(') #Adiciona na pilha -> ['(']
        elif simbolo == ')':
            if len(pilha) > 0: #Verifica se tem '(' na pilha
                pilha.pop() #Remove o seu "par"
            else:
                pilha.append(')') #Se a pilha estiver vazia, significa que há um ')' sem um '(' correspondente
                break

    if len(pilha) == 0:
        print('Expressão válida')
    else:
        print('Expressão inválida')

main()
