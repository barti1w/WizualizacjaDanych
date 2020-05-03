import numpy as np
def generuj(n,m):
    a = np.array([n**x for x in range(1,m+1)])
    return(a)

a=generuj(1,4)
print(a)
