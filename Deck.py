from Card import Card
import random

class Deck:
    def __init__(self):
        self.cards = [Card("kreuz", "Ass", 11), Card("pik", "Ass", 11), Card("herz", "Ass", 11), Card("karo", "Ass", 11),
                 Card("kreuz", "2", 2), Card("pik", "2", 2), Card("herz", "2", 2), Card("karo", "2", 2),
                 Card("kreuz", "3", 3), Card("pik", "3", 3), Card("herz", "3", 3), Card("karo", "3", 3),
                 Card("kreuz", "4", 4), Card("pik", "4", 4), Card("herz", "4", 4), Card("karo", "4", 4),
                 Card("kreuz", "5", 5), Card("pik", "5", 5), Card("herz", "5", 5), Card("karo", "5", 5),
                 Card("kreuz", "6", 6), Card("pik", "6", 6), Card("herz", "6", 6), Card("karo", "6", 6),
                 Card("kreuz", "7", 7), Card("pik", "7", 7), Card("herz", "7", 7), Card("karo", "7", 7),
                 Card("kreuz", "8", 8), Card("pik", "8", 8), Card("herz", "8", 8), Card("karo", "8", 8),
                 Card("kreuz", "9", 9), Card("pik", "9", 9), Card("herz", "9", 9), Card("karo", "9", 9),
                 Card("kreuz", "10", 10), Card("pik", "10", 10), Card("herz", "10", 10), Card("karo", "10", 10),
                 Card("kreuz", "Bube", 10), Card("pik", "Bube", 10), Card("herz", "Bube", 10), Card("karo", "Bube", 10),
                 Card("kreuz", "Dame", 10), Card("pik", "Dame", 10), Card("herz", "Dame", 10), Card("karo", "Dame", 10),
                 Card("kreuz", "Koenig", 10), Card("pik", "Koenig", 10), Card("herz", "Koenig", 10), Card("karo", "Koenig", 10),
                 ]

    def shuffle(self):
        random.shuffle(self.cards)

    def drawCard(self):
        return self.cards.pop()


