#remember the really cool tech of how you can use local variables in a class method so that its for the cool shi but isnt attribute

import card

def intersection_tuples(smaller, bigger):
    intersected = []
    bigger = list(bigger)

    for item in smaller:
        if item in bigger:
            bigger.remove(item)
            intersected.append(item)

    return tuple(intersected)

class SimplifiedCard:

    plays_possible = []

    def __init__(self, cards: card.CardGen):
        self.simple_cards = []

        for card in cards:
            self.simple_cards.append((card.rank, card.suit))

        self.simple_ranks = [rank for rank, suit in self.simple_cards]
        self.simple_suits = [suit for rank, suit in self.simple_cards]


        self.simple_cards_arranged_by_rank = list(sorted(self.simple_cards, key = lambda x: x[0]))

        self.plays = {
            "High Card" : [(1), [15, 1]],
            "Pair" : [(1, 1), [15, 2]],
            "Triple" : [(1, 1, 1) ,[15, 3]],
            "Mini Straight" : [(1, 2, 3), [35, 2]],
            "Impossible" : [(1, 1, 1, 1, 1), [50, 4]]
            }
    
    def play(self, play_name):

        self.cards_by_rank = [rank for rank, suit in self.simple_cards_arranged_by_rank]

        self.play_copy = self.plays[play_name][0]

        if play_name == "High Card":
            return True

        self.adder = 0
        while True:

#                                       ( the play but incremented                  )   (your cards)                 (the play but incremented                    )
            if intersection_tuples(tuple(rank + self.adder for rank in self.play_copy), self.cards_by_rank) == tuple((rank + self.adder for rank in self.play_copy)): #make more efficent one year
                self.play_copy = tuple(rank + self.adder for rank in self.play_copy) #for debugs
                return True
            else:
                self.adder += 1
                if any(card > 13 for card in tuple(rank + self.adder for rank in self.play_copy)):
                    return False



        # for i in range(len(self.cards)):
        #     while True:
        #         if self.cards[i][0] > 0:
        #             self.cards = [(rank[0] - 1,) for rank in self.cards]
        #         else:
        #             break

            
        #     if all(card in self.plays[play_name][0] for card in self.cards):
        #         return "Works"
        #     else:
        #         continue


if __name__ == "__main__":
    hand = card.Deck().deck_52(return_result = True)

    simplified_hand = SimplifiedCard(hand)
    print(simplified_hand.play("Impossible"))
    # print(simplified_hand.play_copy)
    print(simplified_hand.cards_by_rank)
    # print(simplified_hand.adder)