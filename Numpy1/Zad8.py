import numpy as np

def funkcja1(n):
    b=np.array([[2+2*(abs(x-c)) for x in range(n)]for c in range(n)])
    return b

a=funkcja1(8)

def funkcja(n,kierunek):
    poziom=int(n.shape[0])
    pion=int(n.shape[1])
    if poziom%2!=0 or pion%2!=0:
        return "Nie wolno"

    if kierunek == "pionowo":
        a=(n[:,range(0,int(pion/2))])
        return a

    if kierunek == "poziomo":
        a=(n[range(0,int(poziom/2)),:])
        return a
    

b=funkcja(a,"poziomo")
print(b)
