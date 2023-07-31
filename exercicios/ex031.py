km = float(input("Qual a distância da sua viagem? "))
if km <= 200:
    passagem = 0.50 * km
    print(f"Você está prestes a começar uma viagem de {km:.0f}Km")
    print(f"Sua passagem custará R${passagem}")
elif km > 200:
    passagem = 0.45 * km
    print(f"Você está prestes a começar uma viagem de {km:.0f}Km")
    print(f"Sua passagem custará R${passagem}")
    