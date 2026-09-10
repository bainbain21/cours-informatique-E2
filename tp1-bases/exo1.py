# calcul d'IMC

poids = float(input("entrer votre poids (kg) : "))
taille = float(input("entrer votre taille (m) : "))

IMC = poids/(taille*taille)

print(f"votre IMC est de {IMC}")