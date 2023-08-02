from datetime import date
ano_nascimento = int(input("Digite seu ano de nascimento: "))
idade = date.today().year - ano_nascimento
tempo_falta = 18 - idade
tempo_atraso = idade - 18
if idade < 18:
    print(f'Você ainda irá se alistar para o serviço militar, para isso faltam {tempo_falta} anos')
elif idade == 18:
    print("Você já deve se alistar para o serviço militar")
elif idade > 18:
    print(f"Você já está atrasado {tempo_atraso} anos para o alistamento para o")