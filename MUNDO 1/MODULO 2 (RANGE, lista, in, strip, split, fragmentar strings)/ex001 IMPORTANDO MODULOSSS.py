import math
numero = int(input('Digite um numero: '))
raiz = math.sqrt(numero)
floor = math.floor(numero)
ceil = math.ceil(numero)
trunc = math.trunc(numero)
hypotenuza = math.hypot(numero)

print('A raiz de {} é igual a {:.2f}'.format(numero, raiz))
print('A raiz de {} é igual a {}'.format(numero, math.ceil(raiz)))

#posso adicionar o modulo dentro do .format como no exemplo acima
