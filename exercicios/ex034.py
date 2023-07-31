salario = float(input('Informe o seu salário: R$'))
if salario <= 1250:
    aumento = (15/100 * salario) + salario
    print(f'O seu salário após o reajuste de 15% é de R${aumento}')
if salario > 1250:
    aumento = (10/100 * salario) + salario 
    print(f'O seu salário após o reajuste de 10% é de R${aumento}')
    