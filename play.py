#remember the really cool tech of how you can use local variables in a class method so that its for the cool shi but isnt attribute
import card

class SimplifiedCard:

    plays_possible = []

    def __init__(self, cards: card.CardGen): #cards needs to be plural; multiple items
        self.simple_cards = []

        for card in cards:
            self.simple_cards.append((card.rank, card.suit))

        self.simple_cards_arranged_by_rank = list(sorted(self.simple_cards, key = lambda x: x[0]))
        print(self.simple_cards_arranged_by_rank)

        self.plays = {
            "High Card" : [( (1, 1) ), [15, 1], "Jewish"],
            "Pair" : [( (1, 1),  (1, 1) ), [15, 2], "Multiple"],
            "Triple" : [( (1, 1), (1, 1), (1, 1) ), [15, 3], "Multiple"],
            "Mini Straight" : [( (1, 1), (2, 1), (3, 1) ), [35, 2], "Sequential"],
            "Impossible" : [( (1, 1), (1, 1), (1, 1), (1, 1), (1, 1) ), [50, 4], "Multiple"],
            "Flush" : [( (1, 1), (1, 1), (1, 1), (1, 1), (1, 1) ), [50, 5], "Suit"]
            }


    
    def play(self, play_name):

        adder = 0
        init_adder = 0
        play_copy = self.plays[play_name][0]
        temp_simple_cards = self.simple_cards.copy()
        print(temp_simple_cards)


        if play_name == "High Card":
            return True
        
        if self.plays[play_name][2] == "Multiple":

            for rank_check, suit_check in play_copy:
                adder = 0
                print(f"ITERATION: {1 + ( len(self.simple_cards) - len(temp_simple_cards))}")

                while True:
                    print(f" card: {rank_check + init_adder, suit_check + adder} \n adder: {adder} \n if found? {(rank_check + init_adder, suit_check + adder) in temp_simple_cards}")

                    if (rank_check + init_adder, suit_check + adder) in temp_simple_cards:

                        temp_simple_cards.remove((rank_check + init_adder, suit_check + adder))
                        break

                    else:
                        adder += 1

                        if adder >= 4:

                            if len(self.simple_cards) - len(temp_simple_cards) == 0:

                                init_adder += 1
                                adder = 0
                                if init_adder >= 13:
                                    return "Jewslam"

                            else:
                                return "No such card, I'm afraid."

                        
            return True if len(temp_simple_cards) == len(self.simple_cards) - len(play_copy) else False




        if self.plays[play_name][2] == "Suit":

            for (rank_check_useless, suit_check), (rank_mirror, suit_useless) in zip(play_copy, temp_simple_cards):
                print(f"ITERATION: {1 + ( len(self.simple_cards) - len(temp_simple_cards))}")

                while True:
                    if (rank_mirror + adder, suit_check) in temp_simple_cards:

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