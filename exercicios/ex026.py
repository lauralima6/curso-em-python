frase = str(input("Digite uma frase: ")).replace("á","a").replace("à", "a").replace("â", "a").replace("ã", "a").lower().strip()
print('A letra A aparece {} vezes na frase'.format(frase.count('a')))
print('A primeira letra A aparece na posição {}'.format(frase.find('a')+1))
print('A última letra A aparece na posição {}'.format(frase.rfind('a')+1))

