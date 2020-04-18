def Fibb():
    a=0
    b=1
    
    for index in range(999):
        if index==0:
            yield a    
        if index==1:
            yield b        
        if index>0:
            yield a+b
            temp=b
            b=a+b
            a=temp

                   

F=Fibb()
print(next(F))
print(next(F))
print(next(F))
print(next(F))
print(next(F))
print(next(F))
print(next(F))
print(next(F))
print(next(F))
print(next(F))
print(next(F))
print(next(F))