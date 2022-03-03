from datetime import date
nascimento = int(input('Ano de nascimento: '))
atual = date.today().year
categoria = atual - nascimento
print('O atleta tem {} anos'.format(categoria))
if categoria <= 9:
    print('Classificação: MIRIM')
elif categoria <= 14:
    print('Classificação: INFANTIL')
elif categoria <= 19:
    print('Classificação: JUNIOR')
elif categoria <= 25:
    print('Classificação: SENIOR')
else:
    print('MASTER')
