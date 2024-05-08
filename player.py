# deck of cards
# player + dealer hands

#function to deal cards

#calc total of each hand

#check for winner

#game loop

from deck import Deck

class Player:
    """A class to represent the player in the blackjack game."""
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        card = deck.draw()
        self.hand.append(card)

    def show_hand(self):
        return ", ".join(str(card) for card in self.hand)