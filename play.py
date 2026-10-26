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
        temp_simple_cards = self.simple_cards.copy()

        if play_name == "High Card":
            return True

        if play_name == "Flush":

            for (rank_useless, suit_from_play), (rank_mirror, suit_useless) in zip(self.play_copy, temp_simple_cards):
                self.adder = 0

                while True:

                    print(f" card: {rank_mirror, suit_from_play + self.adder} \n adder: {self.adder} \n if found? {(rank_mirror, suit_from_play + self.adder) in temp_simple_cards} \n")
                    if (rank_mirror, suit_from_play + self.adder) in temp_simple_cards:

                        temp_simple_cards.remove( (rank_mirror, suit_from_play + self.adder) )
                        break
                    else:

                        self.adder += 1
                        if self.adder > 4:
                            return False
                    
            return True


        #flaw in this: it modifies the original play_copy, I dont think permanently, but it still does instead of temporarily shifting the cards' digits to see if they fit the play

        if any(suit for rank, suit in self.play_copy): #checks if the play is a rank only play
            return False #maybe find another way to plug this up?
        else:

            for (rank_from_play, suit_useless), (rank_useless, suit_mirror) in zip(self.play_copy, temp_simple_cards):
                print(f"LOOP START. ITERATION: {1 + ( len(self.simple_cards) - len(temp_simple_cards))}")
                self.adder = 0

                while True:

                    print(f" card: {rank_from_play + self.adder, suit_mirror} \n adder: {self.adder} \n if found? {(rank_from_play + self.adder, suit_mirror) in temp_simple_cards}")
                    if (rank_from_play + self.adder, suit_mirror) in temp_simple_cards: 

                        temp_simple_cards.remove( (rank_from_play + self.adder, suit_mirror))
                        print("BREAKING")
                        break

                    else:

                        self.adder += 1
                        if any(card > 13 for card in tuple(rank_from_play + self.adder for rank_from_play, suit_useless in self.play_copy)):
                            print(f"ITERATION: {1 + ( len(self.simple_cards) - len(temp_simple_cards))}")
                            return False
            return True



if __name__ == "__main__":
    hand = card.Deck().deck_52(return_result = True)

    simplified_hand = SimplifiedCard(hand)
    print(simplified_hand.play("Triple"))
    #print(simplified_hand.play_copy)
    #print(simplified_hand.simple_cards)
    #print(simplified_hand.adder)