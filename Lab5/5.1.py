class Material:
    def __init__ (self,rodzaj,dlugosc,szerokosc):
        self.rodzaj = rodzaj
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc

    def wyswietl_nazwe(self):
        return self.nazwa

class Ubrania(Material):
    def __init__ (self,rozmiar,kolor,dla_kogo,nazwa):
        self.rozmiar=rozmiar
        self.kolor=kolor
        self.dla_kogo=dla_kogo
        self.nazwa=nazwa
    def wyswietl_dane(self):
        return self.rozmiar,self.kolor,self.dla_kogo

class Sweter(Ubrania):
    def __init__ (self,rodzaj_swetra,nazwa):
        self.rodzaj_swetra = rodzaj_swetra
        self.nazwa=nazwa      
    def wyswietl_dane(self):
        return self.rodzaj_swetra

temp = Ubrania("M","czerwony","dla_pan","golf")
print(temp.wyswietl_dane())
print(temp.wyswietl_nazwe())
del temp
temp = Sweter("Golf","nazwa")
print(temp.wyswietl_nazwe())
print(temp.wyswietl_dane())


        
