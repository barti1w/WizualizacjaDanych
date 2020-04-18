from itertools import *

def komb(ile):
    for index in range(ile):
        yield list(combinations('0123456789', 3))[index]

gen = komb(5)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
# arr=[1,2,3,4,5,6,7,8,9,0]
# print (list(combinations(arr, 3)))
        