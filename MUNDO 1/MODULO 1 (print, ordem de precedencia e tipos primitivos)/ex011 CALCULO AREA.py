larg = float(input('A largura da parede: '))
alt = float(input('A altura da parede: '))
area = larg * alt
print('Sua parede tem dimensão de {}x{} e sua área é de {}m²'.format(larg, alt, area))
tinta = area / 2
print('Para pintar essa parede, voce precisa de {}l de tinta'.format(tinta))
