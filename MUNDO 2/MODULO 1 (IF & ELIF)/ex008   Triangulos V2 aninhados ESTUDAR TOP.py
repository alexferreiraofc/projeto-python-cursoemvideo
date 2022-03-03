a = float(input('Primeira reta: '))
b = float(input('Segunda reta: '))
c = float(input('Terceira reta: '))
if a < b + c and b < a + c and c < b + c:
    print('As retas PODEM FORMAR um triangulo! ', end='')
    if a == b == c:
        print('EQUILATERO')
    elif a != b != c != a:  # NESSA PARTE C precisa ser diferente de A   C != a
        print('ESCALENO')
    else:
        print('ISOCELES')
else:
    print('As retas NÃO PODEM FORMAR um triangulo')
