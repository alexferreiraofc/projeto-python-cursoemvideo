a = int(input('Digite um numero inteiro: '))
b = int(input('Digite um segundo numero inteiro: '))
if a > b:
    print('O número {} é maior que {}'.format(a, b))
elif b > a:
    print('O número {} é maior que {}'.format(b, a))
else:
    print('Os número são iguais ou são inválidos! ')
