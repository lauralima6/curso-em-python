num = int(input("Digite um número para verificar se ele é par ou ímpar: "))
resultado = num % 2
if resultado == 0:
    print(f"O número {num} é par")
else:
    print(f"O número {num} é ímpar")
