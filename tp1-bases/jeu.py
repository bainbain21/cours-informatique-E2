import random

valeur = {"T" : 14,"V" : 13,"C" : 12,"D" : 11,"R" : 10,"A" : 9, "2" : 8, "3" : 7, "4" : 6, "5" : 5, "6" : 4, "7" : 3, "8" : 2, "9" : 1}
couleur = ["s", "c", "d", "h"]
V = list(range(1, 15))


score_ordi = 0
score_joueur = 0

def creatDeck():
    cards = {}
    for i in range(12):
        car = ""
        c = random.choice(list(valeur.keys()))
        v = valeur.get(c)
        car += c
        car += random.choice(couleur)
        cards[car]=v
    return cards

deck = creatDeck()
print(f"première carte : {list(deck)[1]}")

for i in range(2,11):
    choice = input("pensez vous que la carte suivante sera plus grande ou plus petite , (+/-) : ")
    j=i+1
    if choice == "+":
        if list(deck.values())[j] > list(deck.values())[i] :
            score_joueur +=1
        if list(deck.values())[j] < list(deck.values())[i] :
            score_ordi +=1
    if choice == "_":
           if list(deck.values)[j] < list(deck.values)[i] :
               score_joueur +=1
           if list(deck.values)[j] > list(deck.values)[i] :
               score_ordi +=1 
    print(f"carte suivant : {list(deck)[i]}")
