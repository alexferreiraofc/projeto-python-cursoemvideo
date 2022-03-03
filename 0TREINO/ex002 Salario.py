a = float(input('Digite o salário atual do funcionário: R$ '))
mais = a + (a * 15 / 100)
menos = a + (a * 10 / 100)
if a <= 1000:
    print('O salário era de \033[1;31mR${:.2f}\033[m ficou \033[1;32m{:.2f}\033[m com o aumento'.format(a, mais))
else:
    print('O salário era de \033[1;31m{:.2f}\033[m ficou \033[01;32m{:.2f}\033[m com o aumento'.format(a, menos))
