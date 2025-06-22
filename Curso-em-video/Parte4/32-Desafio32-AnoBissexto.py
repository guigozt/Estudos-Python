from datetime import date

def main():
    ano = int(input('Digite um ano (AAAA): '))

    if ano == 0:
        ano = date.today().year

    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print(f'O ano {ano} é BISSEXTO')
    else:
        print(f'O ano {ano} NÃO É BISSEXTO')

main()

#Exemplos:

#2000 / 4
#2000    500     TRUE
#-
#0
#============
#2000 / 100
#2000      20    FALSE
#-
#0
#============
#2000 / 400
#2000      5      TRUE
#-
#0
#
#
#1900 / 4
#1900    475     TRUE
#-
#0
#=============
#1900 / 100
#1900      19    FALSE
#-
#0
#==============
#1900 / 400
#1600      4     FALSE
#-
#3



