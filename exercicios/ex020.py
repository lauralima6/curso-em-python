from random import shuffle
import time

lista = []
while True:
    nome = input("Digite o nome do aluno: ")
    lista.append(nome)
    if len(lista) == 5:
        break
shuffle(lista)
print("A ordem de apresentação é: ")
print(lista)