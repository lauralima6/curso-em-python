kmrodados = float(input('Quantos quilômetros o carro rodou durante o período alugado? '))
tempo = int(input('Por quantos dias o carro ficou alugado? '))
preco = (60 * tempo) + (0.15 * kmrodados)
print('O valor do aluguel é de R${:.2f}'.format(preco))