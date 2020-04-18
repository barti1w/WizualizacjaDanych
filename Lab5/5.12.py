def miesiace():
    arr=["Styczeń","Luty","Marzec","Kwiecień","Maj","Czerwiec","Lipiec","Sierpień","Wrzesień","Październik","Listopad","Grudzień"]
    for i in range(11):
        yield arr[i]


mies=miesiace()
print(next(mies))
print(next(mies))
print(next(mies))
