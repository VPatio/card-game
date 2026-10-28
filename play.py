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
            "High Card" : [( (1, 0) ), [15, 1], "Jewish"],
            "Pair" : [( (1, 0),  (1, 0) ), [15, 2], "Multiple"],
            "Triple" : [( (1, 0), (1, 0), (1, 0) ), [15, 3], "Multiple"],
            "Mini Straight" : [( (1, 0), (2, 0), (3, 0) ), [35, 2], "Sequential"],
            "Impossible" : [( (1, 0), (1, 0), (1, 0), (1, 0), (1, 0) ), [50, 4], "Multiple"],
            "Flush" : [( (0, 1), (0, 1), (0, 1), (0, 1), (0, 1) ), [50, 5], "Suit"]
            }


    
    def play(self, play_name):

        adder = 0
        play_copy = self.plays[play_name][0]
        temp_simple_cards = self.simple_cards.copy()
        print(temp_simple_cards)


        if play_name not in self.plays.keys():
            raise Exception("Play not real")

        if play_name == "High Card":
            return True
        
        if self.plays[play_name][2] == "Multiple":

            for (rank_check, suit_check_useless), (rank_useless, suit_mirror) in zip(play_copy, temp_simple_cards):
                adder = 0
                print(f"ITERATION: {1 + ( len(self.simple_cards) - len(temp_simple_cards))}")

                while True:
                    if (rank_check + adder, suit_mirror) in temp_simple_cards:

                        print(f" card: {rank_check + adder, suit_mirror} \n adder: {adder} \n if found? {(rank_check + adder, suit_mirror) in temp_simple_cards}")
                        temp_simple_cards.remove((rank_check + adder, suit_mirror))
                        break

                    else:

                        adder += 1
                        if adder > 13:
                            return "No such card, I'm afraid."
            return True if len(temp_simple_cards) == len(self.simple_cards) - len(play_copy) else False

        if self.plays[play_name][2] == "Suit":

            for (rank_check_useless, suit_check), (rank_mirror, suit_useless) in zip(play_copy, temp_simple_cards):
                print(f"ITERATION: {1 + ( len(self.simple_cards) - len(temp_simple_cards))}")

                while True:
                    if (rank_mirror, suit_check + adder) in temp_simple_cards:

                        print(f" card: {rank_mirror, suit_check + adder} \n adder: {adder} \n if found? {(rank_mirror, suit_check + adder) in temp_simple_cards}")
                        temp_simple_cards.remove((rank_mirror, suit_check + adder))
                        break

                    else:

                        adder += 1
                        if adder > 4:
                            return "No such card, I'm afraid."
            return True if len(temp_simple_cards) == len(self.simple_cards) - len(play_copy) else False
        





if __name__ == "__main__":
    hand = card.Deck().deck_52(return_result = True)

    simplified_hand = SimplifiedCard(hand)
    print(simplified_hand.play("Impossible"))
    #print(simplified_hand.play_copy)
    #print(simplified_hand.simple_cards)
    #print(simplified_hand.adder)