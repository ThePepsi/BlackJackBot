import unittest, random

import Card, Deck, NoCardsLeftError

def createRandomCard() -> Card:
    col = random.choice["kreuz","pik","herz","karo"]
    (num, points) = random.choice[("1",1),("2",2),("3",3),("4",4),("5",5),("6",6),("7",7),("8",8),("9",9),("10",10),("Bube",10),("Dame",10),("Koenig",10)]
    return Card(color=col, num=num, points=points)

class Test_Deck(unittest.TestCase):

    def test_Card(self):
        col = random.choice["kreuz","pik","herz","karo"]
        (num, points) = random.choice[("1",1),("2",2),("3",3),("4",4),("5",5),("6",6),("7",7),("8",8),("9",9),("10",10),("Bube",10),("Dame",10),("Koenig",10)]
        x = Card(color=col, num=num, points=points)

        self.assertTrue(hasattr(x,"color"), msg="Deck should have an Attribute called 'color'")
        self.assertTrue(hasattr(x,"num"), msg="Deck should have an Attribute called 'num'")
        self.assertTrue(hasattr(x,"points"), msg="Deck should have an Attribute called 'points'")

        self.assertEqual(x.color, col, f"Color should be: '{col}'")
        self.assertEqual(x.num, num, f"Number should be: '{num}'")
        self.assertEqual(x.points, points, f"The Points should be '{points}'")

    def test_Deck(self):
        x = Deck()
        self.assertTrue(hasattr(x,"cards"), msg="Deck should have an Attribute called 'cards'")

        # Not Sure if no equls method programmed
        c = createRandomCard()
        self.assertTrue((c in x.cards), msg=f"Deck should have a card with {c.col},{c.num}")

    def test_Deck_drawCard(self):
        x = Deck()
        c = x.drawCard()

        self.assertTrue((c is not None), msg="Card drawen should be not null")

        self.assertTrue((c not in x.cards), msg="If a card is drawn, it should not be in the Deck anymore")
       
        
    def test_Deck_shuffle(self):
        x = Deck()
        y = Deck()

        x.shuffle()

        dif = False

        while((len(x.cards) != 0) and (len(y.cards) != 0)):
            if x.drawCard() != y.drawCard():
                dif = True
                break
        
        self.assertTrue(dif, msg="If i shuffle one Deck, it shuld draw other Cards then a not shuffeld Deck")

    def test_Deck_darwCard_Error(self):
        x = Deck()

        for z in range(14*4):
            x.drawCard()

        self.assertTrue((len(x.cards) == 0), msg="All cards should be drawn")

        with self.assertRaises(NoCardsLeftError):
            x.drawCard()

