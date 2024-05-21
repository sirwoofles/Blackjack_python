# game.py

from shoe import Shoe
from player import Player
from dealer import Dealer

import time
import os

class Game:
    def __init__(self, player_name, initial_stack, num_decks = 3):
        self.shoe = Shoe(num_decks)
        self.player = Player(player_name, initial_stack)
        self.dealer = Dealer()
        self.has_hit = False
    
    # function: clear terminal
    def clear_terminal(self):
        if os.name == 'nt':
            _ = os.system('cls')
        else:
            _ = os.system('clear')

    # GAME EVENTS ===============================================================================
    # GAME EVENT: reset_round 
    def reset_round(self):
        self.player.clear_hand()
        self.dealer.clear_hand()
        self.has_hit = False

    # GAME EVENT: DEAL CARDS TO PLAYER AND DEALER
    def initial_deal(self):
        self.player.add_card(self.shoe.deal_card())
        self.dealer.add_card(self.shoe.deal_card())
        self.player.add_card(self.shoe.deal_card())
        self.dealer.add_card(self.shoe.deal_card())

    # GAME EVENT: PLAYER BLACKJACK WIN
    def player_blackjack_win(self):
        return self.player.get_hand_value == 21
    
    # GAME EVENT: PLAYER'S TURN
    def player_turn(self):
        print()
        print(f"{self.player.name}'S TURN")
        while self.player.get_hand_value() < 21:
            action = input("Do you want to HIT, STAND or DOUBLE? (H/S/D)\n").upper()
            if action == "H":
                self.player.hit(self.shoe.deal_card())
                self.has_hit = True
                print(self.player.show_hand())
                if self.player.get_hand_value() > 21:
                    print(f"{self.player.name} busts!")
                    break
            
            elif action == "S":
                self.player.stand()
                break

            elif action == "D":
                if self.has_hit:
                    print("You cannot double after hitting!")
                    continue
                try:
                    self.player.double_bet()
                    self.player.hit(self.shoe.deal_card())
                    print(self.player.show_hand())
                    break
                except ValueError as e:
                    print(e)

            else:
                print("Invalid Action. Please choose H/S/D.")
            print()

    # GAME EVENT: DEALER'S TURN 
    def dealer_turn(self):
        while self.dealer.get_hand_value() < 17:
            self.dealer.hit(self.shoe.deal_card())
            print(self.dealer.show_hand())

    # GAME EVENT: CHECK OUTCOME, D bust, P bust, D-P push, D>P, P>D
    def check_outcome(self):
        player_value = self.player.get_hand_value()
        dealer_value = self.dealer.get_hand_value()

        if dealer_value > 21:
            print(f"Dealer busts ! {self.player.name} wins!")
            self.player.win_bet()

        elif player_value > dealer_value:
            print(f"{self.player.name} wins!")
            self.player.win_bet()

        elif player_value < dealer_value:
            print(f"{self.player.name} loses!")
            self.player.lose_bet()

        else:
            print(f"It's a push!")
            self.player.push_bet()

    # GAME EVENT: manages the blackjack round.
    def play_round(self):
        self.clear_terminal()
        print(f"Player {self.player.name} has {self.player.stack} in the stack.")

        bet_amount = int(input(f"Hello {self.player.name}! Please enter amount you wish to bet this round.\n"))
        self.player.place_bet(bet_amount)
        print(f"{self.player.name} placed a bet of {self.player.bet}. Remaining Stack: {self.player.stack}")

        self.initial_deal()

        print("\nShowing hands of the player and the dealer")
        print(self.player.show_hand())
        print(self.dealer.show_one_card())

        if self.player_blackjack_win():
            print("CONGRATS on BLACKJACK WIN!!")
            self.player.blackjack_win()
        else:
            self.player_turn()
            
            if self.player.get_hand_value() <= 21:
                self.dealer_turn()
                print("\nFinal Hands:")
                print(self.dealer.show_hand())
                print(self.player.show_hand())
                self.check_outcome()

        print(f"\nEnd of round. {self.player.name}'s stack: {self.player.stack}")
        print("================================================================")

    def play_game(self):
            while self.player.stack > 0:
                time.sleep(5)
                self.play_round()
                self.reset_round()
                time.sleep(5)

            print("Game over. Thank you for playing!")


def main():
    name = input("What's your name?: ")
    amount = int(input("How much is your starting stack of money: "))
    game = Game(player_name=name, initial_stack=amount)
    game.play_game()

if __name__ == "__main__":
    main()