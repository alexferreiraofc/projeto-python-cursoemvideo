from math import radians, sin, cos, tan
a = float(input('Digite o angulo: '))
s = sin(radians(a))
print('O angulo de {} tem o SENO de {:.2f}'.format(a, s))
c = cos(radians(a))
print('O angulo de {} tem o Cosseno de {:.2f}'.format(a, c))
t = tan(radians(a))
print('O angulo de {} tem a tangente de {:.2f}'.format(a, t))
