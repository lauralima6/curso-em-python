valor = float(input('Quanto você possui na carteira? '))
convert_dolar = valor / 4.81
convert_euro = valor / 5.27
print('O valor de R${:.2f} convertido para dólar corresponde a U${:.2f} e a €{:.2f}'.format(valor, convert_dolar, convert_euro))