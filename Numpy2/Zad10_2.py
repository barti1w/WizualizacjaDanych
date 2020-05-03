import numpy as np

b = np.array([[x for x in range(9)]for x in range(9)])
print(b)
b=b.reshape(3,27)
print(b)
b=b.reshape(27,3)
print(b)
