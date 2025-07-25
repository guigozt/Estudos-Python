# Modularização ------------------------------------
#import Funcoes -> Importa do módulo (arquivo com as funções)

# Pacotes/Bibliotecas ------------------------------
from Uteis import Numeros #Importa de Uteis (pasta) o pacote Numeros (com o arquivo __init__ que contem as funções)

n = int(input('Número: '))
print(f'Fatorial de {n} = {Numeros.fatorial(n)}')
print(f'Dobro de {n} = {Numeros.dobro(n)}')
