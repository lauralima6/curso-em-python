salario = float(input('Digite o valor do seu salário: R$'))
aumento = salario + (salario * 15/100)
print('O salário do funcionário é R${:.2f}, após o aumento de 15% seu salário será de R${}, tendo um aumento de R${:.2f}'.format(salario, aumento, (aumento-salario)))