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
            return self.show_first()
        
    def hand_val(self):
        """Calculate the total value of the dealer's hand."""
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
    
    def should_draw_card(self):
        """Determine if the dealer should draw another card (hit) based on their current hand."""
        return self.hand_val() < 17
    
        
    
    