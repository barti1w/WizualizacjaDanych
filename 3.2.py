import random as r
macierz=([r.randint(0,10) for i in range(4)],[r.randint(0,10) for i in range(4)],[r.randint(0,10) for i in range(4)],[r.randint(0,10) for i in range(4)])
lista = [macierz[i][j] for i in range(4) for j in range(4) if i==j]
print(lista)
print(macierz)