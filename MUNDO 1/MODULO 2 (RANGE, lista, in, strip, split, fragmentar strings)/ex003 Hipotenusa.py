from math import hypot
a1 = float(input('Digite o angulo do cateto oposto: '))
a2 = float(input('Digite o angulo do cateto adjacente: '))
hp = hypot(a1, a2)
print('O angulo oposto é {}, o angulo adjacente é {}, e a hipotenusa é {:.2f}'.format(a1, a2, hp))
