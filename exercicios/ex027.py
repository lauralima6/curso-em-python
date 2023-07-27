nome = str(input("Digite seu nome completo: ")).strip()
separa = nome.split()
print("Analisando seu nome...")
print("Seu primeiro nome é {} e o seu último nome é {}".format(separa[0], separa[-1]))