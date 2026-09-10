# conversion d'années humaines en années cannines

while True :
    age = int(input("entrer l'âge à convertir : "))
    if age < 0 :
        print ("vous devez entrer un âge positif")
    if age > 0 :
        break

def can(a):
    cannin = 0
    for i in range(a):
        if i < 2 :
            cannin += 10.5
        else :
            cannin += 4
    return cannin 

print(f"votre age cannin est : {can(age)}")