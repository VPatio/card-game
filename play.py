import card
from collections import Counter

class SimplifiedCard:
    simple_converter_rank = {'Ace' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9, '10' : 10, 'Jack' : 11, 'Queen' : 12, 'King' : 13}
    simple_converter_suit = {'Spades' : 1, 'Hearts' : 2, 'Clubs' : 3, 'Diamonds' : 4}

    def __init__(self, cards: card.CardGen):
        self.simple_cards = []

        for card in cards:
            self.simple_rank = self.simple_converter_rank[card.rank]
            self.simple_suit = self.simple_converter_suit[card.suit]

            self.simple_cards.append((self.simple_rank, self.simple_suit))

        self.simple_ranks = [self.simple_card[0] for self.simple_card in self.simple_cards]
        self.simple_suits = [self.simple_card[1] for self.simple_card in self.simple_cards]

        self.rank = 0
        self.suit = 0

        self.plays = {
            (self.rank) : [[15, 1], "High Card"],
            (self.rank, self.rank) : [[15, 2], "Pair"],
            (self.rank, self.rank, self.rank) : [[15, 3], "Triple"],
            (self.rank, self.rank+1, self.rank+2) : [[35, 2], "Mini Straight"],
            (self.rank, self.rank, self.rank, self.rank, self.rank) : [[50, 4], "Impossible"]
            }
        
    def eligible_plays(self):
        all_eligible_plays: list = []

        for (card, amount), (card_valid_no_purpose, amount_valid), (useless_chips, name) in zip(
        Counter(self.simple_cards).items(), 
        Counter(self.plays.keys()).items(),
        self.plays.values()
         ):
            self.rank = card
            if amount >= amount_valid:
                all_eligible_plays.append(name)
        
        if all_eligible_plays == None:
            return "No eligible plays"
        return all_eligible_plays
    

if __name__ == "__main__":
    hand = card.Deck().deck_52(return_result = True)

    simplified_hand = SimplifiedCard(hand)
    #print(simplified_hand.simple_cards)
    print(simplified_hand.eligible_plays())