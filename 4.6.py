class Slowa:
    slowo1 = "mtka"
    slowo2 = "tamak"
    
    def czy_palindrom(self):
        if self.slowo1 == "".join(reversed(self.slowo1)):
            return 1
        else:
            return 0

    def wyswietl(self):
        return self.slowo1,self.slowo2

    def czy_metagramy(self):
        n=0
        for i in range(len(self.slowo1)):
            if self.slowo1[i]!=self.slowo2[i]:
                n=n+1        
        if n==1:
            return "tak"
        else:
            return "nie"

    def czy_anagramy(self):        
        for i in range(len(self.slowo1)):
            a=0
            for j in range(len(self.slowo2)):
                if self.slowo1[i] == self.slowo2[j]:
                    a=a+1
                if j==len(self.slowo2)-1 and a==0:
                    return "nie"
        return "tak"







obiekt = Slowa()
print(obiekt.czy_palindrom())
print(obiekt.wyswietl())
print(obiekt.czy_anagramy())