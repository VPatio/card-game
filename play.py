#remember the really cool tech of how you can use local variables in a class method so that its for the cool shi but isnt attribute
import card

class SimplifiedCard:

    plays_possible = []

    def __init__(self, cards: card.CardGen): #cards needs to be plural; multiple items
        self.simple_cards = []

        for card in cards:
            self.simple_cards.append((card.rank, card.suit))

        self.simple_cards_arranged_by_rank = list(sorted(self.simple_cards, key = lambda x: x[0]))
        self.simple_ranks = [rank for rank, suit in self.simple_cards]

        self.plays = {
            "High Card" : [( (0, 0) ), [15, 1], "Jewish"],
            "Pair" : [( (0, 0),  (0, 0) ), [15, 2], "Multiple"],
            "Triple" : [( (0, 0), (0, 0), (0, 0) ), [15, 3], "Multiple"],
            "Mini Straight" : [( (0, 0), (1, 0), (2, 0) ), [35, 2], "Sequential"],
            "Impossible" : [( (0, 0), (0, 0), (0, 0), (0, 0), (0, 0) ), [50, 4], "Multiple"],
            "Flush" : [( (0, 0), (0, 0), (0, 0), (0, 0), (0, 0) ), [50, 5], "Suit"]
            }


    
    def play(self, play_name):

        play_copy = self.plays[play_name][0]
        temp_simple_ranks = self.simple_ranks.copy()
        checker = 1
        print(self.simple_ranks)

        if play_name == "High Card":
            return True
        
        if self.plays[play_name][2] == "Multiple":

            while True:
                breaker = False

                for _ in range(len(play_copy)):

                    if breaker == True:
                        break

                    while True:

                        if checker in temp_simple_ranks:
                            temp_simple_ranks.remove(checker)

                            if _ == len(play_copy) - 1:
                                return True
                            
                            break

                        else:

                            checker += 1

                            if checker > 13:
                                return False
                            
                            breaker = True
                            break
                








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

    def __str__(self):
        return str(self.simple_cards)


if __name__ == "__main__":

    hand = card.Deck.make_hand(card.Deck(), 10, return_result = True)


    simplified_hand = SimplifiedCard(hand)
    print(simplified_hand)
    print(simplified_hand.play("Pair"))
    #print(simplified_hand.play_copy)
    #print(simplified_hand.simple_cards)
    #print(simplified_hand.adder)