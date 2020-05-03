import numpy as np

def funkcja(n):
    a=[x for x in range(n,0,-1)]
    b=np.diag([x for x in range(n,0,-1)])


    return b

a=funkcja(3)
print(a)