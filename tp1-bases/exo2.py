list = []
i = 1
while i > 0 :
    i = int(input("entrer un nombre entier : "))
    if i > 0:
        list.append(i)

def moy(liste) :
    den = 0
    num = 0
    for el in liste :
        num += el
        den += 1
    moyenne = num/den
    return moyenne

print(f"la liste trié est {list.sort()}")    
print(f"le maximum est {max(list)}")
print(f"le minimum est {min(list)}")
print(f"la moyenne est {moy(list)}")