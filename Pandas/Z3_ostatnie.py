import pandas as pd
import numpy as np
import xlrd
import openpyxl

df= pd.read_csv("zamowienia.csv",header=0,delimiter=";")

def siedem(df):    
    p=df.copy()
    p['Rok']=pd.DatetimeIndex(p['Data zamowienia']).year
    cztery=p[p["Rok"]==2004].copy()
    cztery=cztery.drop(['Rok'],axis=1)
    cztery.to_csv('zamowienia_2004.csv',header=True, index=False)
    pic=p[p["Rok"]==2005].copy()
    pic=pic.drop(['Rok'],axis=1)
    pic.to_csv('zamowienia_2005.csv',header=True, index=False)

siedem(df)