# Maria vrea să verifice dacă greutatea şi înălţimea ei corespund vârstei pe care o are. Ea
# a găsit într-o carte următoarele formule de calcul ale greutăţii şi înălţimii unui copil, v
# fiind vârsta : greutate=2*v+8 (în kg), înălţime=5*v+80 (în cm). Realizaţi un program
# care să citească vârsta unui copil şi să afişeze greutatea şi înălţimea ideală, folosind
# aceste formule.
# Notez: greutatea= m; înălțimea=h 
v=int(input('Introdu vârsta copilului:'))
m=2*v+8
h=5*v+80
print('Greutatea ideală a copilului la vârsta de', v , 'ani ar fi' , m , 'kilograme' )
print('Înălțimea ideală a copilului la vârsta de' , v , 'ani ar fi de', h , 'centimetri' )