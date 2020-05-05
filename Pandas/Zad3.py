import pandas as pd
import numpy as np
import xlrd
import openpyxl

xlsx=pd.ExcelFile("F:\Pyy\Pandas\zamowienia.xlsx")
df=pd.read_excel(xlsx,"Arkusz3")

def jeden(df):
    for Sprzedawca in df['Sprzedawca'].unique():
        print(Sprzedawca)
    

def dwa(df):
    a=df.sort_values('Utarg',ascending=False)
    return a.head(5)

def trzy(df):
    a=df.set_index(["Sprzedawca","idZamowienia"]).count(level="Sprzedawca")    
    return a

def cztery(df):
    a=df.set_index(["Kraj","idZamowienia",'Sprzedawca','Data zamowienia']).count(level="Kraj")  
    return a

def piec(df):
    dff=df[df["Kraj"]=="Polska"]     
    dfff=dff[dff["Data zamowienia"]>='20050101']
    b=dfff[dfff["Data zamowienia"]<='20051231']
    a=b.set_index(["Kraj","idZamowienia",'Sprzedawca','Data zamowienia']).count(level="Kraj")
    return a

def szesc(df):
    df=df[df["Data zamowienia"]>'20031231']
    df=df[df["Data zamowienia"]<='20041231']
    df=df.mean(axis = 0) 
    return df.tail(1)




a=szesc(df)
print(a)