a = str(input('Digite uma frase: ')).strip().lower()
print('A letra A aparece {} vezes na frase.'.format(a.count('a')))
print('A primeira letra A apareceu na posição {}'.format(a.find('a')))
print('A última letra A apareceu na posição {}'.format(a.rfind('a')+1))

#o +1 é opcional, pessoas fora da área vão ler a primeira letra começando pelo numero 1
