a = float(input('Tamanho da primeira reta: '))
b = float(input('Tamanho da segunda reta: '))
c = float(input('Tamanho da terceira reta: '))
if a < b + c and b < a + c and c < a + b:
    print('\033[1;32mAs retas PODEM formar um triangulo\033[m')
else:
    print('\033[1;31mAs retas NÃO podem formar um Triangulo!\033[m')
