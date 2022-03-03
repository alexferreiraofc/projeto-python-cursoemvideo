#\033   [0;               33;                    44m #padrão ANSI
#       [ style,          text,                     background          m
#       0- none            30 -branco             40 - branco
#       1- bold            31 -vermelho           41 - vermelho
#       4- underline___    32 - verde             42 - verde
#       7- negative        33 - amarelo           43 - amarelo
#                          34 - azul              44 - azul
#                          35 - roxo              45 - roxo
#                          36 - ciano             46 - ciano
#                          37 - cinza             47 - cinza
#PADRÃO ANSI

# ---------      \033[0;33;44m
print('\033[1;31mOlá, mundo!\033[m')
print('Olá, \033[4;34mAlex\033[m, seja bem vindo!')
#Posso usar um dicionário de cores em uma variavel com chaves {} POR EXEMPLO:
nome = 'Alex'
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7;30m'}
print('Olá {}{}{}, seja bem vindo ao mundo Python!'.format(cores['azul'], nome, cores['limpa']))
