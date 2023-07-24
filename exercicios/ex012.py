preco = float(input('Qual o valor do produto? R$'))
desconto = preco - (preco * (5/100))
print('O produto que custava R${:.0f}, com 5% de desconto vai custar R${:.2f}'.format(preco, desconto))
