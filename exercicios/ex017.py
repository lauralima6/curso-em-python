# co = float(input("Digite o comprimento do cateto oposto: "))
# ca = float(input("Digite o comprimento do cateto adjacente: "))
# hipotenusa = (co ** 2 + ca ** 2) ** (1/2)
# print("O tamanho da hipotenusa é: {:.2f}".format(hipotenusa))

import math
co = float(input("Digite o comprimento do cateto oposto: "))
ca = float(input("Digite o comprimento do cateto adjacente: "))
hi = math.hypot(co, ca)
print("O tamanho da hipotenusa é: {:.2f}".format(hi))