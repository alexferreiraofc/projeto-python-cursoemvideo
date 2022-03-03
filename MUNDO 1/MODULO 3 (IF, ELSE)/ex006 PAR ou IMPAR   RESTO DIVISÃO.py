numero = int(input('Digite um número para saber se é par ou impar: '))
resto = numero % 2

if resto == 0:
    print('O numéro {} é par'.format(numero))
else:
    print('O número {} é Impar'.format(numero))
