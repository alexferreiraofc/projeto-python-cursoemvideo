a = int(input('Diga qual o tamanho da primeira reta: '))
b = int(input('Diga qual é o tamanho da segunda reta: '))
c = int(input('Diga qual é o tamanho da terceira reta: '))
if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima PODEM formar um TRIANGULO!')
else:
    print('Os segmentos acima NÃO podem formar um Triangulo!')


#A soma de 2 lados tem que ser maior que a "base" do triangulo, para poder formar um triangulo
# por exemplo, 3, 3, 3(3+3 = 6) ou seja 6 é maior que 3, então é possível formar um triangulo.
# agora, 2, 2, 5(2+2 = 4) ou seja NÃO pode formar um triangulo, pq a soma de 2 lados é menor que a "base/modulo"
