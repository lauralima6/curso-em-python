# import random 
# import time
# n1 = input("Digite o nome do primeiro aluno: ")
# n2 = input("Digite o nome do segundo aluno: ")
# n3 = input("Digite o nome do terceiro aluno: ")
# n4 = input("Digite o nome do quarto aluno: ")
# n5 = input("Dgite o nome do quinto aluno: ")
# lista = [n1, n2, n3, n4, n5]
# escolhido = random.choice(lista)
# print("Sorteando um nome...")
# time.sleep(1.5)
# print("...")
# time.sleep(2.5)
# print("O nome sorteado foi: {}".format(escolhido))

import random 
import time
lista = []
while True:
    nome = input("Digite o nome do aluno: ")
    lista.append(nome)
    if len(lista) == 5:
        break
escolhido = random.choice(lista)
print("Sorteando um aluno...")
time.sleep(1.5)
print("O aluno sorteado foi: {}".format(escolhido))