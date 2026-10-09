import random

class CardValue:
        def __init__(self, value_txt:str, value_pts:int):
            self.value_txt=value_txt
            self.value_pts=value_pts

class CardColor:
        def __init__(self,shade:str, shade_name:str, foreground_color:str, background_color:str):
               self.shade=shade
               self.shade_name=shade_name
               self.foreground_color=foreground_color
               self.background_color=background_color

class Card:
        def __init__(self,CardValue,CardColor):
              self.CardValue = CardValue
              self.CardColor = CardColor

        def __str__(self):
                return f"{self.CardValue.value_txt} {self.CardColor.shade}"

        def __gt__(self,other):
                print(other)
                return self.CardValue.value_txt > other.CardValue.value_txt
        
        def __lt__(self,other):
                return self.CardValue.value_txt < other.CardValue.value_txt
        
        def __le__(self,other):
                return self.CardValue.value_txt <= other.CardValue.value_txt
        
        def __ge__(self,other):
                return self.CardValue.value_txt >= other.CardValue.value_txt
        
        def __eq__(self,other):
                return self.CardValue.value_txt == other.CardValue.value_txt
        
        def __ne__(self,other):
                return self.CardValue.value_txt != other.CardValue.value_txt


class Deck:
        def __init__(self, dict_card, list_color):
                self.dict_card = dict_card
                self.list_color = list_color
                self.cards = self.init52_cards()

        def init52_cards(self):
                deck = []
                for col in self.list_color:
                        for k,v in self.dict_card.items():
                                cv = CardValue(v,k)
                                cc = CardColor(col["symbol"],col["name"],col["color"],"")
                                deck.append(Card(cv,cc))
                return deck

        def shuffle(self):
                deckshuf = list(self.cards.items())
                random.shuffle(deckshuf)
                self.cards = dict(deckshuf)

        def draw(self):
                return self.cards[0]

        def discard(self):
                self.cards.popitem()