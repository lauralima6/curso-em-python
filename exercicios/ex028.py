import random 

def jogo_advinhacao():
    
    num_min = 0
    num_max = 100
    
    num_pensado = random.randint(num_min, num_max)
    
    print(f"Eu pensei em um número entre {num_min} e {num_max}.")
    
    tentativas = 0
    while True:
        tentativa = int(input("Tente adivinhar o número que pensei: "))
        tentativas += 1
        
        if tentativa < num_pensado:
            print("Tente um número maior!")
        elif tentativa > num_pensado:
            print("Tente um número menor!")
        else:
            print(f"Parabéns, você acertou! O número pensado foi {num_pensado} ")
            break
        if tentativas >= 10 and tentativa != num_pensado:
            print(f"Você perdeu! Eu pensei no número {num_pensado}.")
            break
            
if __name__ == "__main__":
   jogo_advinhacao()