import card

hand = card.Deck()
hand.deck_52()

print(f"Your hand: {hand.make_hand(5, return_result = True)} \nRest of the deck: {hand.deck}")
print(f"New hand: {hand.make_hand(5, return_result = True)} \nRest of the deck: {hand.deck}")
print(f"Resetting deck: {hand.reset_deck(return_result = True)}")