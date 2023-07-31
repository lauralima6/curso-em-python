r1 = float(input("Tamanho da primeira reta: "))
r2 = float(input("Tamanho da segunda reta: "))
r3 = float(input("Tamanho da terceira reta: "))

if r1 < r2 + r3 and r3 < r2 + r1 and r2 < r3 + r1: 
    print("As retas podem formar um triângulo.")
else: 
    print("As retas não podem formar um triângulo.")