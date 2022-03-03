n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d))
print('Adivisão inteira é {} e a potencia {}'.format(di, e))

#variante do print com quebra de linha

print('A soma é {}, \n o produto é {} e a \n divisão é {}'.format(s, m, d), end=' ')