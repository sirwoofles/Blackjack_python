# test_player_dealer_hand.py
"""
Comments:
    1. double function doesnt work: still lets me hit/double after initial Double (DONE)
    2. if dealer bust, never update win conditions (DONE)
    3. check win conditions and lose conditions and push conditions (DONE)
    4. show dealers hands after every round(DONE)
    5. blackjack! u win! (DONE)
    6. blackjack win payout (DONE)
    7. ACE doesnt -10 from total hand when total > 21 (DONE)
    8. cannot double after hitting.(DONE)
"""

from shoe import Shoe
from player import Player
from dealer import Dealer
import time
import os

def clear_terminal():
    # Clear command for Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # Clear command for Linux and MacOS
    else:
        _ = os.system('clear')


def test_game():
    #clear_terminal()

    # Create the Shoe
    print("Creating a Shoe with 3 shuffled decks...")
    shoe = Shoe(3)
    print(f"Shoe created with {len(shoe.cards)} cards.")

    # Create a player with initial stack and a dealer
    print()
    print("Creating player('Ian' , 1000) and dealer")
    player = Player("Ian", 1000)
    dealer = Dealer()

    while player.stack > 100:
        time.sleep(2)
        #clear_terminal()
        print(f"Player {player.name} has {player.stack} in the stack.")
        # place a bet
        print()
        print("Player Ian places 100 bet")
        player.place_bet(100)
        print(f"{player.name} placed a bet of {player.bet}. Remaining Stack: {player.stack}")

        # Deal 2 cards to the player and the dealer
        print()
        print("Dealing 2 cards to the player and dealer....")
        player.add_card(shoe.deal_card())
        dealer.add_card(shoe.deal_card())
        player.add_card(shoe.deal_card())
        dealer.add_card(shoe.deal_card())

        # show hands
        print()
        print("Showing hands of the player and the dealer")
        print(player.show_hand())
        print(dealer.show_one_card())

        # NOT YET IMPLEMENTED BUY INSURANCE
        """
        # check if dealer's face-up card is face card
        if dealer.face_up_card_is_face_card():
            print("Dealer's face-up card is a face card.  Option to buy Insurance.")
            try:
                player.buy_insurance()
                print(f"{player.name} bought insurance. Remaining stack: {player.stack}")
            except ValueError as e:
                print(e)
        """

        # PLAYER Blackjack WIN
        if player.get_hand_value() == 21:
            print("Congrats on BLACKJACK WIN!!")
            player.blackjack_win()

        #player actions
        print()
        has_hit = False
        print("Player actions: (H)Hit, (D)Double, (S)Stand")
        while player.get_hand_value() < 21:
            action = input ("Do you want to hit, stand, double? (H/S/D)\n").upper()
            if action == 'H':
                player.hit(shoe.deal_card())
                has_hit = True
                print(player.show_hand())
                if player.get_hand_value() > 21:
                    print(f"{player.name} busts!")
                    break

            elif action == "S":
                player.stand()
                break

            elif action == "D":
                if has_hit == True:
                    print("You cannot double after hitting!")
                    continue
                try:
                    player.double_bet()
                    player.hit(shoe.deal_card())
                    print(player.show_hand())
                    break
                except ValueError as e:
                    print(e)
            
            else:
                print("Invalid Action. Please choose H/S/D.")

            print()

        # if player hands exceed 21, lose bet
        if player.get_hand_value() > 21:
            print()
            print(dealer.show_hand())
            print(f"{player.name} lost the round, lose {player.bet}")
            player.lose_bet()
            print(f"End of round. {player.name}'s stack: {player.stack}")
            player.clear_hand()
            dealer.clear_hand()
            continue
            
        print()

        # else, player hand < 21 and proceeds to dealer's turn, dealer stands on soft 17
        while dealer.get_hand_value() < 17:
            dealer.hit(shoe.deal_card())
            print(dealer.show_hand())

        print()
        print("Final Hands:")
        print(dealer.show_hand())
        print(player.show_hand())

        print()
        # Determine the outcome
        if dealer.get_hand_value() > 21:
            print(f"Dealer busts! {player.name} wins!")
            player.win_bet()

        elif player.get_hand_value() > dealer.get_hand_value():
            print(f"{player.name} wins!")
            player.win_bet()
        
        elif player.get_hand_value() < dealer.get_hand_value():
            print(f"{player.name} loses!")
            player.lose_bet()

        else:
            print("It's a push!")
            player.push_bet()

        print()
        print(f"End of round. {player.name}'s stack: {player.stack}")
        print("================================================================")
        print()
        player.clear_hand()
        dealer.clear_hand()
        time.sleep(3)

def main():
    test_game()

if __name__ == "__main__":
    main()