#Un brăduţ este împodobit cu globuleţe albe, roşii şi albastre. Numărul globuleţelor albe se citeşte de la tastatură. Câte globuleţe are brăduţul, ştiind că numărul de
#globuleţe roşii este cu 3 mai mare decât numărul de globuleţe albe, iar globuleţele
#albastre sunt cu 2 mai puţine decât totalul celor albe şi roşii. Exemplu: Date de intrare:
#12 Date de ieşire: 52.
# Notăm: globulețele albe=a; globulețele roșii= r; globulețele albastre=y;
a=int(input('Introduceți numărul de globulețe albe:'))
r=a+3
print('Numărul de globulețe roșii este:', r)
y=(a+r)-2 
print('Numărul de globulețe albastre este:', y)
total=a+r+y
print('Pe brăduț sunt', total, 'globulețe' ) 
