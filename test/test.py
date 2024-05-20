from src.shoe import Shoe

def test_shoe():
    print("Creating a shoe with 1 decks...")
    shoe = Shoe(1)
    print(f"Shoe created with {len(shoe.cards)} cards.")

    print("Shuffling the shoe...")
    shoe.shuffle()

    print("Dealing 5 cards from the shoe:")
    for _ in range(5):
        card = shoe.deal_card()
        print(card)
    
    print(f"Remaining cards in shoe: {len(shoe.cards)}")

def main():
    test_shoe()

if __name__ == "__main__":
    main()