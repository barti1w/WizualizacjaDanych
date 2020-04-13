lista=[i for i in range(50) if i%4==0]
plik = open("Cw1.txt","w+")
plik.writelines(str(lista))
plik.close()