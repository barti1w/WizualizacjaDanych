class ciag:

    a1 = 0
    r = 1
    n = 1

    def wyswietl_dane(self):       
        return self.a1,self.n,self.r

    def pobierz_elementy(self,a1,a2,a3):
        self.a1=a1
        self.a2=a2
        self.a3=a3


    def pobierz_parametry(self,a1,n,r):
        self.a1=a1
        self.n=n
        self.r=r

    def policz_sume(self):
        return ((((2*self.a1+((self.n-1)*self.r))*0.5))*self.n)

    def policz_elementy(self):
        lista = [self.a1+self.r*i for i in range(self.n)]
        return lista


obiekt = ciag()
obiekt.pobierz_parametry(1,5,1)
print(obiekt.policz_elementy())
print(obiekt.policz_sume())
print(obiekt.wyswietl_dane())
obiekt.pobierz_elementy(1,2,3)