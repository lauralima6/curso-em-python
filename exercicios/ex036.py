valor_casa = float(input("Informe o valor da casa: R$"))
salario = float(input("Inform o valor do seu salário: R$"))
tempo = float(input("Em quantos anos você deseja pagar a casa? "))
prestacao = valor_casa / (tempo*12) 
teto = (30/100 * salario) 
if prestacao > teto:
    print("Empréstimo negado! O valor da prestação não pode exceder 30% do seu salário.")
else:
    print(f"Empréstimo aprovado! O valor da sua prestação mensal será de R${prestacao:.2f}")