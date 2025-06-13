def salario(hr, vlr):
    return hr * vlr

def main():
    numeroFuncionario = int(input('Número funcionário: '))
    horasTrabalhadas = int(input('Horas trabalhadas: '))
    valorHora = float(input('Valor pela hora trabalhada: '))

    print(f'NUMBER = {numeroFuncionario}')
    print(f'SALARY = R$ {salario(horasTrabalhadas, valorHora):.2f}')

main()
