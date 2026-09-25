import random
import unicodedata

life = 5

def strip_accents(s):
   return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')

with open("dic.txt", 'r', encoding='utf-8') as f :
    lignes = f.readlines()
    ligne_al = random.choice(lignes)
    mot = ligne_al.strip()

mot = strip_accents(mot.upper())
i = 0
p=list(mot)
pendu = []
for el in mot :
    if i == 0 : 
        i=1
        pendu += [el]
    else : pendu += ["_"]
print("".join(pendu))
#print("".join(p))


def ajout(pendu,life,p):
    l = input("entrer une lettre : ")
    i=0
    vie = 0

    if l in pendu:
                print("lettre déjà soumise")
    elif l not in p:
            life-=1

    for _ in pendu :
        if l.upper() == p[i] :
            pendu[i]=p[i]
            i+=1
        else :
            i+=1
    print("".join(pendu)) 

    print(f"il te reste {life} vie(s)")
    return pendu,life

while life !=0 and pendu != p :
    pendu , life = ajout(pendu,life,p)

print("bien joué")