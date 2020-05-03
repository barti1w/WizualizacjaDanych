import numpy as np

b = np.arange(12)
print(b)
b=b.reshape(3,4)
for a in b.flat:   
   print(a)

b=b.reshape(4,3)
for a in b.flat:   
   print(a)

b=b.reshape(2,6)
for a in b.flat:   
   print(a)
