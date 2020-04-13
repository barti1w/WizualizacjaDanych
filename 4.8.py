class Robaczek:

    def __init__ (self,x,y,krok):
        self.x=x
        self.y=y
        self.krok=krok

    def idz_w_gore(self,ile_krokow):
        self.y=self.y+self.krok*ile_krokow
        
    def idz_w_dol(self,ile_krokow):
        self.y=self.y-self.krok*ile_krokow

    def idz_w_prawo(self,ile_krokow):
        self.x=self.x+self.krok*ile_krokow

    def idz_w_lewo(self,ile_krokow):
        self.x=self.x-self.krok*ile_krokow
  
    def gdzie(self):
        return self.x,self.y

   
    
        
obiekt = Robaczek(0,0,2)
obiekt.idz_w_dol(2)
print(obiekt.gdzie())
obiekt.idz_w_prawo(6)
print(obiekt.gdzie())
del obiekt
print(obiekt.gdzie())