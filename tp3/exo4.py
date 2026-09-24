import random

with open("dic.txt", 'r', encoding='utf-8') as f :
    lignes = f.readlines()
    ligne_aleatoire = random.choice(lignes)
    mot = ligne_aleatoire.strip()

mot = mot.upper()
i = 0
pendu = []
for el in mot :
    if i == 0 : 
        i=1
        pendu += [el]
    else : pendu += ["_"]
print("".join(pendu))