n = int(input('Digite um número inteiro: '))
print("MENU DE OPÇÕES \n Escolha uma das opções abaixo para ser a base da conversão: \n 1 - BINÁRIO \n 2 -OCTAL \n 3 - HEXADECIMAL")
opcao = int(input("Sua escolha: "))
if opcao == 1: 
    print("Seu número convertido para binário é {}".format(bin(n))) 
if opcao == 2:
    print("Seu número convertido para octal é {}".format(oct(n)))
if opcao == 3:
    print("Seu número convertido para hexadecimal é {}".format(hex(n)))
