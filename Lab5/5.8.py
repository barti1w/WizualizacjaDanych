class samogloski:
    
    def __init__(self, data):
        if isinstance(data,str)==True:
            self.data = data
            self.index = len(data)
            self.ind = -1
            self.zmienna = -1
        else:
            pass
    
    def __iter__(self):
        return self

    def __next__(self):
        samo = ["a","i","o","u","e"]
        for i in range(self.index):           
            self.ind = self.ind + 1
            if self.ind==self.index:
                raise StopIteration
            if self.data[self.ind] in samo:            
                return self.data[self.ind]
        # else:
        #     self.ind = self.ind + 1
        #     if self.data[self.ind] in samo:
        #         return self.data[self.ind]                
        #     else:
        #         self.ind = self.ind + 1
        #         if self.data[self.ind] in samo:
        #             return self.data[self.ind]
                    

cos = samogloski("samogloskiooaa")
cos.__iter__()
print(cos.__next__())
print(cos.__next__())
print(cos.__next__())
print(cos.__next__())
print(cos.__next__())
print(cos.__next__())
print(cos.__next__())
print(cos.__next__())
print(cos.__next__())
print(cos.__next__())
print(cos.__next__())
print(cos.__next__())
print(cos.__next__())
print(cos.__next__())



