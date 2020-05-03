import numpy as np

def funkcja(n):
    a=np.array([[x for x in range(0+n*x,n+n*x)]for x in range(n)])
    return a

a=funkcja(3)
b=funkcja(4)
print(a.min(axis=1))
print(a.min(axis=0))

print(b.min(axis=1))
print(b.min(axis=0))