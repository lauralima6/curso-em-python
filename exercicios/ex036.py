valor_casa = float(input("Informe o valor da casa: R$"))
salario = float(input("Inform o valor do seu salário: "))
tempo = float(input("Em quantos anos você deseja pagar a casa? "))
prestacao = valor_casa / (tempo*12) 
teto = salario - (30/100 * salario) 
if prestacao > teto:
    print("Empréstimo negado! O valor da prestação não pode exceder 30% do seu salário.")
else:
    print("Empréstimo aprovado!")