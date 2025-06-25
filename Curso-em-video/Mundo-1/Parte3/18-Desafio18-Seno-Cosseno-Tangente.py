def main():
    from math import sin, cos, tan, radians

    angulo = float(input('Digite o angulo: '))
    seno = sin(radians(angulo))
    cosseno = cos(radians(angulo))
    tangente = tan(radians(angulo))

    print(f'O angulo de {angulo} tem SENO de {seno:.2f}')
    print(f'O angulo de {angulo} tem COSSENO de {cosseno:.2f}')
    print(f'O angulo de {angulo} tem TANGENTE de {tangente:.2f}')

main()
