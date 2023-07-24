largura = float(input('Qual a largura da sua parede? '))
altura = float(input('Qual a altura da sua parede? '))
area = largura * altura
qtd_tinta = area / 2
print('A sua parede tem {}m², a quantidade de tinta necessária para pintá-la é {:.0f} litros'.format(area, qtd_tinta))
