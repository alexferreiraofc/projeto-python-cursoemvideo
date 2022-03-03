if carro.esquerda():
    Bloco True

else:
    Bloco False

#   if / else vão ser usados em condições compostas, se não somente sera usado o comando IF em condição simples.
Exemplo :

tempo = int(input('Quantos anos tem o seu carro? '))
if tempo <=3:
    print('Carro novo')
else:
    print('Carro velho')
print('--FIM--')
#-----------------------------------VARIAÇÃO--------------------------
tempo = int(input('Quantos anos tem o seu carro? '))
print('Carro novo' if tempo <=3 else 'Carro velho')  #Modo simplifcado mas não funcional pois fica tudo muito condensado
print('--FIM--')

#________________________________________________________________________
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Sua média foi boa, parabéns!')
else:
    print('Voce está abaixo da média, atenção!')
