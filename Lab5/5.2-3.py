class Ksztalty:
    
    def __init__(self, x, y):        
        self.x=x 
        self.y=y
        self.opis = "To będzie klasa dla ogólnych kształtów"

    def pole(self):
        return self.x * self.y

    def obwod(self):
        return 2 * self.x + 2 * self.y

    def dodaj_opis(self, text):
        self.opis = text

    def skalowanie(self, czynnik):
        self.x = self.x * czynnik
        self.x = self.y * czynnik


class Kwadrat(Ksztalty):

    def __init__(self, x):
        self.x = x
        self.y = x

    def __str__(self):
        return 'Kwadrat o boku {}'.format(self.x)
    
    def __add__(self,other):
        return 4*self.x+4*other.x

    def __ge__(self,other):
        if self.x!=other.x:
            return "{} != {}".format(self.x,other.x)
        else:
            return "źle"
    def __gt__(self,other):
        return "{} >= {}".format(self.x,other.x)
    def __le__(self,other):
        return "{} <= {}".format(self.x,other.x)
    def __lt__(self,other):
        if self.x<other.x:
            return "To-> {} jest mniejsze od tego-> {}".format(self.x,other.x)
        else:
            return "To-> {} jest mniejsze od tego-> {}".format(other.x,self.x)
kw1 =Kwadrat(2)
kw2=Kwadrat(1)
print(kw1)
suma=Kwadrat(kw1+kw2)
print(suma)
print(kw1<kw2)
print(kw2!=kw1)