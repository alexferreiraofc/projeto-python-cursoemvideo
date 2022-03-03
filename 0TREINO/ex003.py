from random import randint
nome = str(input('Qual é o seu nome? ')).strip().lower()
numero = int(input('\033[1;31mTente advinhar o número que eu estou pensando entre 0 e 5....\033[m '.format(nome)))
aleatorio = randint(0, 5)
if nome == aleatorio:
    print('\033[32mVoce me derrotou o número que eu pensei era {}\033[m'.format(aleatorio))
else:
    print('\033[1;31mVoce errou, EU venci, o número era {}\033[m'.format(aleatorio))
