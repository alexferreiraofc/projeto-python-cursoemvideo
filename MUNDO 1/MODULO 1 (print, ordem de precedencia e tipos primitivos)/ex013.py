salario = float(input('Qual o valor do salário atual do funcionário? R$ '))
reajuste = salario + (salario * 15 / 100)
print('O salario desse funcionário era de R${:.2f} com o reajuste de 15% ficou em R$ {:.2f}'.format(salario, reajuste))
