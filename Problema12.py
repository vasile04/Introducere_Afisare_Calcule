# .Într-o gospodărie sunt 4 găini. Introduceţi în calculator prin variabilele a, b, c, d
# numărul de ouă pe care-l dă fiecare găină într-o zi. Afişaţi câte ouă se obţin într-o
# săptămână.
# Notez: s=suma de ouă în fiecare zi; t= totalul de ouă timp de o săptămână
a=int(input('Introdu numărul de ouă pe care-l dă prima găină într-o zi: '))
b=int(input('Introdu numărul de ouă pe care-l dă a 2-ua găină în fiecare zi: '))
c=int(input('Introdu numărul de ouă pe care-l dă a 3-ia găină în fiecare zi: '))
d=int(input('introdu numărul de ouă pe care-l dă a 4-a găină în fiecare zi:'))
s=a+b+c+d
t=7*(a+b+c+d)
print('Într-o săptămână se vor obține', t,  'ouă' )

