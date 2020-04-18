def Parzyste(data):
    for index in range(0,len(data),2):
        yield data[index]

gen = Parzyste("Feliks")
print(next(gen))
print(next(gen))
print(next(gen))
