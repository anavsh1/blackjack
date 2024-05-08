from deck import Deck, Card

class Dealer:
    def __init__(self):
        self.hand = []

    def draw(self, deck):
        card = deck.draw()
        self.hand.append(card)

    def show_first(self):
        if self.hand:
            return str(self.hand[0])
        else:
            return "No cards dealt yet."

    def show_hand(self, reveal_all=False):
        """Show the dealer's hand. If `reveal_all` is False, show only the first card."""
        if reveal_all:
            return ", ".join(str(card) for card in self.hand)
        else:
            return self.show_first_card()
        
    
    