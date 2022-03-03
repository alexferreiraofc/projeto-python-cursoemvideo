dias = int(input('Quantos dias voce vai alugar? '))
km = float(input('Quantos KM vc rodou? '))
dk = (dias * 60) + (km * 0.15)
print('O total a pagar é {}'.format(dk))
