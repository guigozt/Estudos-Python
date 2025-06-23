def main():
    salario, mesesMax, resgateMin = map(float, input().split())
    valorMin, tempo, porcentagem = map(float, input().split())

    if salario >= valorMin and mesesMax <= tempo:
        valorFinal = salario + (salario * porcentagem / 100)

        if valorFinal >= resgateMin:
            print('invista!')
            return
    
    print('nao invista!')
    
main()
