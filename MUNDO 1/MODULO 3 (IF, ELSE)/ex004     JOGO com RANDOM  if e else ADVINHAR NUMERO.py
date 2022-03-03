import random
nome = str(input('Qual é o seu nome? ')).strip().title()
numero = int(input('Tente advinhar um número entre 0 e 5, {}! '.format(nome)))
aleatorio = [0, 1, 2, 3, 4, 5]
escolha = random.choice(aleatorio)
if escolha == numero:
    print('{} Voce acertou o numero {}. Parabéns!'.format(nome, escolha))
else:
    print('{} Voce errou o número era {}. Tente novamente.'.format(nome, escolha))

#_________________________ VERSÃO DO PROFESSOR \/_________________________________________________________________

from time import sleep
from random import randint
computador = randint(0, 5) #faz o computador "pensar"< ATENÇÃO A ESSE COMANDO RANDOM, ELE FAZ COM QUE A MAQUINA RANDOM UM INT ENTRE PARENTESES
print('-=-' * 20)
print('vou pensar em um numero entre 0 e 5. Tente advinhar...')
print('-=-' * 20)
jogador = int(input('Em que numero eu pensei? ')) # jogador tenta advinhar
print('PROCESSANDO..')
sleep(2)
if jogador == computador:
    print('Parabens! Voce conseguiu me vencer!')
else:
    print('Ganhei! eu pensei no numero {} e nao no {}'.format(computador, jogador))
