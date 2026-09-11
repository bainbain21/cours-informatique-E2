import exo1, exo2, exo3, exo4, exo5, exo7, revision_ex1

print("quel exercice voulez vous voir ?")
exo = int(input(" 1 - IMC \n 2 - moyenne d'une liste \n 3 - années chiens \n 4 - approximation de pi \n 5 - comversion decimal en binaire \n 6 - calculatrice \n 7 - plaque d'immatriculation\n"))

if exo == 1 :
    exo1.exo1()
elif exo == 2 : 
    exo2.exo2()
elif exo == 3 :
    exo3.exo3()
elif exo == 4 :
    exo4.exo4()
elif exo == 5 :
    exo5.exo5()
elif exo == 6 :
    revision_ex1.exo6()
elif exo == 7 :
    exo7.exo7()