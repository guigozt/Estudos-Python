altura = float(input('Informa a altura da parede (Metros): '))
largura = float(input('Informa a largura da parede (Metros): '))
area = altura * largura
tintaNec = area / 2

print(f'Sua parede tem a dimenão de: {largura:.2f}X{altura:.2f} e sua área é de {area:.2f}m²')
print()
print(f'Para essa parede, você precisará de {tintaNec:.2f}L de tinta')
