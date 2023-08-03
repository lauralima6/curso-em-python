n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))
media = (n1 + n2)/2
if media < 5:
    print('Reprovado! Sua média ficou abaixo de 5 pontos.')
if media >= 5 and media < 7:
    print(f'Você irá para a recuperação! Sua média foi {media}')
if media >= 7:
    print(f'Aprovado! Sua média foi {media}')
    