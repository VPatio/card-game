#remember the really cool tech of how you can use local variables in a class method so that its for the cool shi but isnt attribute
import card

class SimplifiedCard:

    plays_possible = []

    def __init__(self, cards: card.CardGen): #cards needs to be plural; multiple items
        self.simple_cards = []

        for card in cards:
            self.simple_cards.append((card.rank, card.suit))

        self.simple_cards_arranged_by_rank = list(sorted(self.simple_cards, key = lambda x: x[0]))

        self.plays = {
            "High Card" : [( (1, 0) ), [15, 1]],
            "Pair" : [( (1, 0),  (1, 0) ), [15, 2]],
            "Triple" : [( (1, 0), (1, 0), (1, 0) ), [15, 3]],
            "Mini Straight" : [( (1, 0), (2, 0), (3, 0) ), [35, 2]],
            "Impossible" : [( (1, 0), (1, 0), (1, 0), (1, 0), (1, 0) ), [50, 4]],
            "Flush" : [( (0, 1), (0, 1), (0, 1), (0, 1), (0, 1) ), [50, 5]]
            }


    
    def play(self, play_name):

        self.adder = 0
        
        self.play_copy = self.plays[play_name][0]

        if play_name == "Flush":
            if all(suit==self.simple_cards[0][1] for rank, suit in self.simple_cards): #checks all cards, but I only need it to check 5. Solution: use adder and for loop
                return True
            else:
                return False

        if play_name == "High Card":
            return True

        #flaw in this: it modifies the original play_copy, I dont think permanently, but it still does instead of temporarily shifting the cards' digits to see if they fit the play
        
        while True:

            if not any(suit for rank, suit in self.play_copy): #checks if the play is a rank only play
                
                if all( (rank + self.adder, 0) in self.simple_cards for rank, suit in self.play_copy): #it basically checks if the hand has even one card, which then the thing while check it over and over, not removing it.
                    return True
                else:

                    self.adder += 1
                    if any(card > 13 for card in tuple(rank + self.adder for rank, suit in self.play_copy)):
                        return False

            else:
                if all( (rank + self.adder, suit) in self.simple_cards for rank, suit in self.play_copy):
                    return True
                else:
                    pass



if __name__ == "__main__":
    hand = card.Deck().deck_52(return_result = True)

    simplified_hand = SimplifiedCard(hand)
    print(simplified_hand.play("Impossible"))
    print(simplified_hand.play_copy)
    print(simplified_hand.simple_cards)
    print(simplified_hand.adder)