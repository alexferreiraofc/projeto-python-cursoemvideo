sal = float(input('Qual salário do funcionário? R$ '))
novo = (sal * 15 / 100) + sal
novo1 = (sal * 10 / 100) + sal
if sal <= 1250:
    print('O antigo salário era R${:.2f} e com o aumento ficou R${:.2f}'.format(sal, novo))
else:
    print('O antigo salário era R${:.2f} e com o aumento ficou R${:.2f}'.format(sal, novo1))



#____________________RESOLUÇÃO DO PROFESSOR________________________
salario = float(input('Qual o salário do funcionario? '))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Quem ganhava {:.2f} passa a ganhar {:.2f} agora.'.format(salario, novo))
