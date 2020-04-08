def funkcja (**zakupy):
    suma=0
    for i in zakupy:
        suma+=zakupy[i]
    return suma


print(funkcja(ołówek=1, olej=5, orzechy=8, akacje=20))