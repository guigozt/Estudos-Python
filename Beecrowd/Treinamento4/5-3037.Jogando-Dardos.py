def main():
    rodadas = int(input('Quantas rodadas? '))
    resultado = []

    for _ in range(rodadas):
        pontosJoao = 0
        pontosMaria = 0

        for jogadas in range(6):
            if jogadas < 3:
                pontos, distancia = input('[JOAO] Pontos e Distancia: ').split()
                pontos, distancia = int(pontos), int(distancia)

                pontosJoao += pontos * distancia
            else:
                pontos, distancia = input('[MARIA] Pontos e Distancia: ').split()
                pontos, distancia = int(pontos), int(distancia)

                pontosMaria += pontos * distancia

        #Apos os 3 arremessos(6) ele compara os pontos
        if pontosJoao > pontosMaria:
            resultado.append('JOAO')
        elif pontosMaria > pontosJoao:
            resultado.append('MARIA')
        else:
            resultado.append('EMPATE')

    for imprime in resultado:
        print(imprime)

main()
