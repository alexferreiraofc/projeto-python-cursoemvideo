p = float(input('Qual seu peso em KG? '))
a = float(input('Qual é a sua altura em Metros? '))
imc = p / (a ** 2)
if imc <= 18.5:
    print('Abaixo do Peso')
elif imc <= 25:
    print('Peso Ideal')
elif imc <= 30:
    print('Sobrepeso')
elif imc <= 40:
    print('Obesidade')
else:
    print('Obesidade Morbida')
print('Seu IMC é {:.2f}'.format(imc))