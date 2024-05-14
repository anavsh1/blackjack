from deck import Deck
from player import Player
from dealer import Dealer

class Blackjack:
    def __init__(self):
        """Initialize the game with players and a dealer."""
        self.deck = Deck()
        self.player = Player(name="Player 1")
        self.dealer = Dealer()
    
    def take_player_turn(self):
        """Allow the player to take actions until they decide to stand or bust."""
        while True:
            print(f"\nYour hand: {self.player.show_hand()} (Value: {self.player.hand_val()})")
            action = input("Choose an action - (H)it or (S)tand: ").strip().lower()

            if action == 'h':
                self.player.draw(self.deck)
                if self.player.hand_val() > 21:
                    print("Bust! You exceed 21.")
                    return
            elif action == 's':
                print("You chose to stand.")
                return
            else:
                print("Invalid input. Please enter 'H' or 'S'.")

    def take_dealer_turn(self):
        """Let the dealer play according to the house rules."""
        print("\nDealer's turn:")
        while self.dealer.should_draw_card():
            self.dealer.draw(self.deck)
        print(f"Dealer's hand: {self.dealer.show_hand(reveal_all=True)} (Value: {self.dealer.hand_val()})")

    
    def determine_results(self):
        """Determine and print the results of the round."""
        player_total = self.player.hand_val()
        dealer_total = self.dealer.hand_val()

        if player_total > 21:
            print("Player busts. Dealer wins.")
            self.player.adjust_chips('lose')
        elif dealer_total > 21 or player_total > dealer_total:
            print("Player wins.")
            self.player.adjust_chips('win')
        elif player_total == dealer_total:
            print("Push. It's a tie.")
        else:
            print("Dealer wins.")
            self.player.adjust_chips('lose')
    
    def play_round(self):
        """Play one round of blackjack."""
        # Initial setup
        self.player.clear_hand()
        self.dealer.hand = []
        self.deck = Deck()
        self.player.place_bet()

        # Initial dealing
        for _ in range(2):
            self.player.draw(self.deck)
            self.dealer.draw(self.deck)

        # Display hands
        print(f"\nDealer shows: {self.dealer.show_first()}")
        print(f"Your hand: {self.player.show_hand()}")

        # Check for immediate blackjack win/loss
        if self.player.has_blackjack():
            print("Blackjack! Player wins.")
            return
        elif self.dealer.hand_val() == 21:
            print("Dealer has Blackjack! Dealer wins.")
            return

        # Player and dealer turns
        self.take_player_turn()
        if self.player.hand_val() <= 21:
            self.take_dealer_turn()
        self.determine_results()

    def play_game(self):
        while True:
            self.play_round()
            if self.player.chips <= 0:
                print("You've run out of chips! Game over.")
                break
            replay = input("\nDo you want to play another round? (Y/N): ").strip().lower()
            if replay != 'y':
                break
        print(f"Thank you for playing!\nYour total winnings are: {self.player.chips}")

if __name__ == "__main__":
    game = Blackjack()
    game.play_game()
