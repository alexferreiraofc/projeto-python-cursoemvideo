print('{:=^40}'.format(' LOJAS FERREIRA '))
price = float(input('Qual valor total das compras? R$ '))
print(''' FORMAS DE PAGAMENTO
[ 1 ] á vista no DINHEIRO
[ 2 ] á vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
option = int(input('Qual é a opção de pagamento? '))
if option == 1:
    total = price - (price * 10 / 100)
elif option == 2:
    total = price - (price * 5 / 100)
elif option == 3:
    total = price
    parcela = total / 2
    print('Sua compra sera parcelada em 2x de R$ {}'.format(parcela))
elif option == 4:
    total = price + (price * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra sera parcelada em {}x de R${:.2f} '.format(totparc, parcela))
else:
    total = price
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')
print('Sua compra de R${:.2f} vai custar R$ {:.2f} no final'.format(price, total))
