import pandas as pd
import numpy as np
import xlrd
import openpyxl

xlsx=pd.ExcelFile("F:\Pyy\Pandas\imiona.xlsx")
df=pd.read_excel(xlsx,"Arkusz1")

def jeden(df):
    return(df[df['Liczba']>1000])

def dwa(df):
    return(df[df['Imie']=="BARTOSZ"])

def trzy(df):
    return(df.agg({'Liczba':['sum']}))

def cztery(df):    
    a=df[((df['Rok']>=2000) & (df['Rok']<=2005))]
    return(a.groupby(['Rok']).agg({'Liczba':['sum']}))

def piec(df):
    return(df.groupby(['Plec']).agg({'Liczba':['sum']}))

def szesc(df):    
    p = df.sort_values("Liczba", ascending=False).groupby(['Rok', "Plec"])
    for i, z in enumerate(p, 1):
        print(f"{z[0]}")
        print(f"{z[1].iloc[[0],[1]].values[0][0]}",
              f"{z[1].iloc[[0],[2]].values[0][0]}")

def siedem(df):
    k=df[df['Plec']=='K']
    m=df[df['Plec']=='M']
    p= k.sort_values("Liczba", ascending=False)
    i=m.sort_values("Liczba", ascending=False)
    return p.head(1),i.head(1)


a = siedem(df)
print(a)
