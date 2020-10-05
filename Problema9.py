# Date trei numere, să se calculeze toate sumele posibile de câte două numere. Afişarea
# să cuprindă şi termenii sumei, nu numai valoarea ei. Exemplu: Date de intrare : 2 13
# 4 Date de ieşire: 2+13 =15 2+4=6 13+4=17.
# Notez: x=primul numar; y=al 2-lea numar; z=al 3-lea numar
x=int(input('Introdu primul numar:'))
y=int(input('Introdu al 2-lea numar:'))
z=int(input('Introdu al 3-lea numar: ')) 
print(x, '+', y, '=', x+y )
print(x, '+', z, '=', x+z)
print(y, '+', z, '=', y+z)
