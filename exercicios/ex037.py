n = int(input('Digite um número inteiro: '))
print("MENU DE OPÇÕES \n Escolha uma das opções abaixo para ser a base da conversão: \n 1 - BINÁRIO \n 2 -OCTAL \n 3 - HEXADECIMAL")
opcao = int(input("Sua escolha: "))
if opcao == 1: 
    print("{} convertido para binário é {:b}".format(n, n)) 
if opcao == 2:
    print("{} convertido para octal é {:o}".format(n, n))
if opcao == 3:
    print("{} convertido para hexadecimal é {}".format(n, hex(n)))
