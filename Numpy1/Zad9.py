import numpy as np
a=0
b=1
fibb=[]
for i in range(25):
    fibb.append(b)
    c=a
    a=b
    b=b+c

a=np.array([[fibb[x] for x in range(0+5*x,5+5*x)]for x in range(5)])
print(a)