nome = str(input('Qual é o seu nome: '))
if nome == 'Alex':
    print('Que nome bonito!'.format(nome))
elif nome == 'Hunter' or nome == 'Avax' or nome == 'Bitcoio':
    print('Esse nome é bem diferente'.format(nome))
elif nome in 'Jordan Mamador Jones Juan':
    print('Nomes mamadores'.format(nome))
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))
