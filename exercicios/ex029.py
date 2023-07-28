velocidade = float(input("Informe a velocidade do carro: "))

if velocidade <= 80:
    print("Tenha um bom dia, dirija com segurança!")
elif velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f"A sua velocidade ultrapassou a velocidade permitida da via, você será multado em R${multa}")
