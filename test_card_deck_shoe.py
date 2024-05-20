# test_card_deck_shoe.py
"""
    remove the shuffles, and the test will print out the shoe/deck in order.
"""

from shoe import Shoe

def test_shoe():
    print("Creating a shoe with 1 deck1...")
    shoe = Shoe(1)
    print(f"Shoe created with {len(shoe.cards)} cards.")

    print("Shuffling the shoe...")
    shoe.shuffle()

    print("Dealing 52 cards from the shoe:")
    for _ in range(52):
        card = shoe.deal_card()
        print(card)
    
    print(f"Remaining cards in shoe: {len(shoe.cards)}")

def main():
    test_shoe()

if __name__ == "__main__":
    main()
