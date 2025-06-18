def animal(t, e, c):
    if t == 'vertebrado' and e == 'ave' and c == 'carnivoro':
        return 'aguia'
    elif t == 'vertebrado' and e == 'ave' and c == 'onivoro':
        return 'pomba'
    elif t == 'vertebrado' and e == 'mamifero' and c == 'onivoro':
        return 'homem'
    elif t == 'vertebrado' and e == 'mamifero' and c == 'herbivoro':
        return 'vaca'
    elif t == 'invertebrado' and e == 'inseto' and c == 'hematofago':
        return 'pulga'
    elif t == 'invertebrado' and e == 'inseto' and c == 'herbivoro':
        return 'lagarta'
    elif t == 'invertebrado' and e == 'anelideo' and c == 'hematofago':
        return 'sanguessuga'
    elif t == 'invertebrado' and e == 'anelideo' and c == 'onivoro':
        return 'minhoca'

def main():
    tipo = input()
    especie = input()
    classe = input()

    print(animal(tipo, especie, classe))

main()
