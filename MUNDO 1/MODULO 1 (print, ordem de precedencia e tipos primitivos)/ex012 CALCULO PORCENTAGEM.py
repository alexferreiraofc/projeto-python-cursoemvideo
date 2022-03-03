preço = float(input('Digite o valor do produto: R$'))
novo = preço - (preço * 5 / 100)
print('O valor do produto era {:.2f}, na promoção com desconto de 5% ficou {:.2f}'.format(preço, novo))


# Na equação já sabemos que a porcen(100)tagem é 5%, mas a formula é dividir o valor do desconto por 100 (x / 100)
