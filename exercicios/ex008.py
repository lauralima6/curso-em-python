metros = int(input('Digite uma distância em metros: '))
km = metros / 1000
cm = metros * 100
mm = metros * 1000
hm = metros / 100 
dam = metros / 10
dm = metros * 10
print('A medida de {:.0f}m corresponde a: \n {:.2f}km \n {:.0f}cm \n {:.0f}mm \n {:.0f}hc \n {:.0f}dc \n {:.0f}dm'.format(metros, km, cm, mm, hm, dam, dm))