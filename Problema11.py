# Măriuca ţine evidenţa iepurilor din crescătorie. Ea îşi notează câţi iepuri sunt la
# începutul fiecărei luni, câţi au murit şi câţi s-au născut în cursul fiecăei luni. Puteţi să
# realizaţi un program care, primind aceste date, să afişeze la sfârşitul fiecărei luni câţi
# iepuri sunt în crescătorie? Exemplu : Date de intrare : nr. Iepuri la început de luna 10
# nr. iepuri morti 2 nr. iepuri nascuti 6 Date de ieşire : 14 iepuri.
# Notez: nr de iepuri la inceput de luna= s; numarul de iepuri morti=m; numarul de iepuri nascuti=n; nr total de iepuri=x;
s=int(input('Introdu numarul de iepuri la inceput de luna:'))
m=int(input('Introdu numarul de iepuri morti:'))
n=int(input('introdu numarul de iepuri nascuti:'))
x=s-m+n
print('În crescătorie sunt', x, 'iepuri' )