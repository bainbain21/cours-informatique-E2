#calculatrice simple

print("opérations : \n a pour addition\n s pour soustraction\n m pour multiplication\n d pour division")
op = input("selectionner l'opération choisie : ")
val1 = float(input("entrer la première valeur : "))
val2 = float(input("entrer la deuxième valeur : "))

i = 0 #gestion d'erreur

if op == "a" :
    res = val1 + val2
    si = "+"
if op == "s" :
    res = val1 - val2
    si = "-"
if op == "m" :
    res = val1 * val2
    si = "*"
if op == "d" :
    if val2 == 0 :
        print("la division par 0 est impossible")
        i = 1 #gestion de l'erreur pour arreter le code
    else :
        res = val1/val2
        si = "/"
if i == 0 :
    print(f"le resultat de {val1} {si} {val2} = {res}")