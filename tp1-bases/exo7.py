# générateur plaque d'immatriculation fr

import random
from random import randrange

def matricul() :

    lettre = ["A","B","C","D","E","F","G","H","J","K","L","M","N","P","Q","R","S","T","V","W","X","Y","Z"]

    A,B,C = random.choices(lettre, k=3)
    if A == "S" or C == "S" and B == "S" :
        B = random.choices(lettre)

    I,II,III = randrange(10),randrange(10),randrange(10)

    D,E,F = random.choices(lettre, k=3)
    if D == "S" or F == "S" and E == "S" :
        E = random.choices(lettre)

    return f"{A}{B}{C}-{I}{II}{III}-{D}{E}{F}"

print(matricul())
