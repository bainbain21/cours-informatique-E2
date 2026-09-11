#calculatrice simple
def exo6() :
    print("opérations : \n a pour addition\n s pour soustraction\n m pour multiplication\n d pour division")

    while True :
        while True :
            liste_op = ["a","s","m","d"]

            op = input("selectionner l'opération choisie : ")
            op = op.lower()
            if op not in liste_op :
                print("opération non comprise")
            else :
                val1 = float(input("entrer la première valeur : "))
                val2 = float(input("entrer la deuxième valeur : "))
                break

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

        rep = input("nouvelle opération ? (o/n) : ")
        if rep == "n" :
            break