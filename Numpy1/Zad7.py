import numpy as np

def funkcja(n):
    b=np.array([[2+2*(abs(x-c)) for x in range(n)]for c in range(n)])
    return b

a=funkcja(7)

print(a)
