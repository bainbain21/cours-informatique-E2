from Deck import *
import random

cards = {"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":11,"Q":12,"K":13,"A":14}
color = [{
    "name" : "spade",
    "symbol": "♠",
    "color" : "black"
    },{
    "name" : "clubs",
    "symbol": "♣",
    "color" : "black"
    },{
    "name" : "clubs",
    "symbol": "♦",
    "color" : "black"
    },{
    "name" : "heart",
    "symbol": "♥",
    "color" : "red"
    }]

score_ordi = 0
score_joueur = 0

deck = Deck(cards,color)
current=deck.draw()
print(current)
print(f"première carte : {current}")

for i in range(9):
    choice = input("pensez vous que la carte suivante sera plus grande ou plus petite , (+/-) : ")
    drawn = deck.draw()
    j=i-1
    if choice == "+":
        if current > drawn :
            score_joueur +=1
        if current < drawn :
            score_ordi +=1
    if choice == "-":
           if current < drawn :
               score_joueur +=1
           if current > drawn :
               score_ordi +=1 

    print(f"carte suivant : {drawn}")
    current = drawn


#current card -> draw new -> current = draw new