# calcul d'IMC
def exo1():
    poids = float(input("entrer votre poids (kg) : "))
    taille = float(input("entrer votre taille (m) : "))

    def IMC(p,t) :
        imc = p/(t*t)
        return imc

    print(f"votre IMC est de {IMC(poids,taille)}")