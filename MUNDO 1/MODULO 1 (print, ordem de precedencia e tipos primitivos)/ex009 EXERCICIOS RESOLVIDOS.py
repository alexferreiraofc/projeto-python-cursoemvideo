import math
#~~~~~~~~~~ EXERCICIO DE ANTECESSOR E SUCESSOR ~~~~~~~~~~~~~~~~~~

a = int(input('Digite um numero: '))
soma = a + 1
menos = a - 1
print('O número {} é antecedido por {} e sucedido por {}'.format(a, soma, menos))

#~~~~~~~~~~~~~~~~~~EXERCICIO DOBRO TRIPLO E RAIZ QUADRADA COM BIBLIOTECA MATH IMPORTADA ~~~~~~~~~~~~~~~~~~~~~~

a = int(input('Digite um numero: '))
d = a * 2
t = a * 3
r = a ** (1/2)
print('O numero {}, o dobro é {}, o triplo é {}, e a raiz dele é {:.2f}'.format(a, d, t, r))

#~~~~~~~~~~~~~~~~~~~~ EXERCICIO MEDIA DO ALUNO ~~~~~~~~~~~~~~~~~~~~

a = float(input('Diga qual sua primeira nota: '))
b = float(input('Diga qual a sua segunda nota: '))
s = (a + b) / 2
print('A nota do aluno na primeira prova foi de {} na segunda foi {} e a média dele é {:.2f}'.format(a, b ,s))


#  ~~~~~~~~ ~~~~~~~~ Exercicio conversão de CM para MM ~~~~~~~~~~~~~~~~~~~~

a = float(input('Digite a metragem: '))
cm = a * 100
mm = a * 1000
print('A metragem {:.2f} convertida para cm {:.2f} e mm {:.2f}'.format(a, cm, mm))

# ~~~~~~~~~~~~~~~~~~ EXERCICIO DE CONVERSÃO DE MOEDAS ~~~~~~~~~~
a = float(input('Quanto reais voce tem: '))
print('R${:.2f} Convertidos em dólares ficaria U${:.2f}'.format(a, a / 3.27))