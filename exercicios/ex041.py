from datetime import date
nascimento = int(input('Digite o seu ano de nascimento: '))
atual = date.today().year
idade = atual - nascimento

if idade <= 9:
    print('O atleta se encaixa na categoria MIRIM')
if idade > 9 and idade <= 14: 
    print('O atleta se encaixa na categoria INFANTIL')
if idade > 14 and idade <= 19:
    print('O atleta se encaixa na categoria JUNIOR')
if idade > 19 and idade <= 25:
    print('O atleta se encaixa na categoria SÊNIOR')
if idade > 25:
   print('O atleta se encaixa na categoria MASTER') 