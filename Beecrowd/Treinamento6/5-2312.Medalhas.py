def ordena(quadro):
    #lambda: função anonima (pode dar qualquer nome, no caso "item")
    #item acessa o item especifico do "quadro" para fazer a ordenação
    #ordem é feita pelo menos importante -> nome,bronze,prata e ouro 
    quadro.sort(key=lambda item: item[0])               #Nome
    quadro.sort(key=lambda item: item[3], reverse=True) #Medalhas Bronze
    quadro.sort(key=lambda item: item[2], reverse=True) #Medalhas Prata
    quadro.sort(key=lambda item: item[1], reverse=True) #Medalhas Ouro
                  
def exibe(quadro):
    for pais, mo, mp, mb in quadro:
        print(pais, mo, mp, mb)

def main():
    qtdPaises = int(input())
    quadroMedalhas = []

    for _ in range(qtdPaises):
        pais, mo, mp, mb = input().split()
        mo, mp, mb = int(mo), int(mp), int(mb)
        quadroMedalhas.append([pais, mo, mp, mb])

    ordena(quadroMedalhas)
    exibe(quadroMedalhas)
    
main()
