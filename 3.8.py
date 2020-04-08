def funkcja (a=1,r=1,ile=10):
    wynik=0
    for i in range(1,ile+1):
        wynik+=a
        a+=r        
    return wynik



print(funkcja())