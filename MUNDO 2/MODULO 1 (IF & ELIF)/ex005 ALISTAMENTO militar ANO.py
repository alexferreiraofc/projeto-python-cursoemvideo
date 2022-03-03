from datetime import date
atual = date.today().year
nasc = int(input('Que ano voce nasceu? '))
idade = atual - nasc
print('Voceu nasceu em {} e tem {} anos de idade'.format(nasc, idade, atual))
if idade < 18:
    saldo = 18 - idade
    ano = atual + saldo
    print('Voce ainda não tem a idade de alistamento, faltam {} anos'.format(saldo))
    print('Seu alistamento será {}'.format(ano))
elif idade == 18: #como não tem variavel aqui, o saldo e o ano vão dar erro de sintaxe.
    print('Voce tem que se alistar IMEDIATAMENTE, ATENÇÃO.')
elif idade > 18:
    saldo = idade - 18
    ano = atual - saldo
    print('Voce já passou {} anos do alistamento obrigatório.'.format(saldo))
    print('Seu alistamento foi em {}'.format(ano))
