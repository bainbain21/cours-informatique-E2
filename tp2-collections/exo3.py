import random

# on créer un tableau contenant n entiers ( 2 < n < 100 ) aléatoires tous compris entre 0 et 500
i=0
n = random.randint(3, 99)
tableau = [random.randint(0, 500) for i in range(n)]
print(tableau)

table = [1,45,2,45]

def dif(tab):
    x=0
    for i in tab:
        if tab.count(i)>1:
            x+=1
    return x

if dif(table) == 0:
    print("touts les entiers sont différents")
else :
    print("certains entiers sont identiques")
