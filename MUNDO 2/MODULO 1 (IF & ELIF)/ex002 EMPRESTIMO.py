casa = float(input('Qual valor do imóvel? R$ '))
salario = float(input('Qual salário do comprador? R$ '))
anos = int(input('Quantos anos de financiamento? '))
presta = casa / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos))
print('A prestação será de R${:.2f}'.format(presta))
if presta <= minimo:
    print('Empréstimo pode ser CONCEDIDO')
else:
    print('Empréstimo NEGADO')



#ex 36 mundo 2 do modulo 1 foi um pouco dificil de lembrar.
#mas observando, devo colocar todas as variaveis no inicio do codigo
