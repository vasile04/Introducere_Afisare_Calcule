# Se introduc de la tastatură trei cifre. Afişaţi pe aceeaşi linie 5 numere formate cu
# aceste cifre luate o singură dată. Exemplu : date de intrare : 3 4 2 Date de ieşire : 324
# 342 243 234 432.
# Notez: primul numar=n; al doilea numar=x; al treilea numar=y
n=int(input('introdu primul numar:'))
x=int(input('introdu al doilea numar:'))
y=int(input('introdu al treilea numar:')) 
print(str(n)+str(x)+str(y), str(x)+str(n)+str(y), str(y)+str(x)+str(n), str(y)+str(n)+str(x))