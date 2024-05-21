# test_player_dealer_hand.py

from shoe import Shoe
from player import Player
from dealer import Dealer

def test_game():
    # Create the Shoe
    print("Creating a Shoe with 1 shuffled deck...")
    shoe = Shoe(1)
    print(f"Shoe created with {len(shoe.cards)} cards.")

    # Create a player with initial stack and a dealer
    print()
    print("Creating player('Ian' , 1000) and dealer")
    player = Player("Ian", 1000)
    dealer = Dealer()

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

    #player actions
    print()
    
    print("Player actions: (H)Hit, (D)Double, (S)Stand, (B)Buy Insurance!!!!")
    while player.get_hand_value() < 21:
        action = input ("Do you want to ")