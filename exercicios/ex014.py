temp = float(input('Forneça a temperatura em Celsius: '))
conversaoF = (temp * 1.8) + 32
conversaoK = temp + 273.15
print('A temperatura de {}°C corresponde a {}°F e a {} K'.format(temp, conversaoF, conversaoK))