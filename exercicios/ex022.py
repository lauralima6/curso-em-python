import time
nome = str(input("Digite seu nome completo: ")).strip()
print("Analisando seu nome...")
time.sleep(1.6)
print("Seu nome em letras maiúsculas é: {}".format(nome.upper()))
time.sleep(1)
print("Seu nome em letras minúsculas é: {}".format(nome.lower()))
time.sleep(1)
print("Seu nome tem ao todo {} letras".format(len(nome) - nome.count(' ')))
separa = nome.split()
time.sleep(1)
print("Seu primeiro nome é {} ele tem {} letras".format(separa[0], len(separa[0])))