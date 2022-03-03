d = float(input('Qual é a distancia da sua viagem? '))
if d <= 200:
    print('O valor da passagem ficou em R${:.2f}'.format(d * 0.50))
else:
    print('O valor da passagem ficou em R${:.2f}'.format(d * 0.45))
