ano = int(input("Informe o ano que deseja analisar: "))
if ano % 4 == 0: 
    print(f"O ano {ano} é bissexto")
else:
    print(f"O ano {ano} não é bissexto")