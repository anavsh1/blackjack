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
    
    def hand_val(self):
        """Calculate the total value of the player's hand."""
        total = 0
        aces = 0

        for card in self.hand:
            total += card.value
            if card.rank == 'Ace':
                aces += 1

        # Adjust value for Aces if the total exceeds 21
        while total > 21 and aces > 0:
            total -= 10
            aces -= 1

        return total

    def clear_hand(self):
        """Clear the player's hand for a new round."""
        self.hand = []

    def has_blackjack(self):
        """Check if the player's hand contains a blackjack (an Ace and a 10-value card)."""
        return self.hand_val() == 21 and len(self.hand) == 2