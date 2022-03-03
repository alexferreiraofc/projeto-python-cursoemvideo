v = int(input('Qual a velocidade do seu carro? '))
multa = (v - 80) * 7
if v > 80:
    print('Voce foi multado em R${:.2f}'.format(multa))
else:
    print('Voce não foi multado.')








#-_______________________________PROFESSOR RESOLUÇÃO_______________________________________________________
velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    print('MULTADO!')
    multa = (velocidade-80) * 7
    print('Voce deve pagar uma multa de R$ {:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com cuidado.')
