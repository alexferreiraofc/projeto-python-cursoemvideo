n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
if media < 5:
    print('Voce foi \033[0;31mREPROVADO\033[m sua media foi \033[0;31m{:.2f}\033[m.'.format(media))
elif 5 <= media <= 7:
    print('\033[0;33mRECUPERAÇÃO\033[m, sua média foi \033[0;33m{:.2f}\033[m'.format(media))
elif media > 7:
    print('\033[0;32mAPROVADO\033[m, sua média foi \033[0;32m{:.2f}\033[m'.format(media))
