import sys
print("Napisz zdanie")
zdanie = input()
literki = list(zdanie)
x=0
for i in literki:
    if i == " ":
        x+=1
print(x)
