#remember the really cool tech of how you can use local variables in a class method so that its for the cool shi but isnt attribute

import card
from collections import Counter

def difference_cards(card_set, rank_or_suit = False):
    if type(rank_or_suit) == bool:
        card_set = tuple(
                    card_set[i+1] - card_set[i]
                    for i in range(len(card_set) - 1)
                )
    else:
        card_set = tuple(
                card_set[i+1][rank_or_suit] - card_set[i][rank_or_suit]
                for i in range(len(card_set) - 1)
            )
    
    return card_set


def intersection_tuples(tuple1, tuple2):
    intersected = []

    for item in tuple1:
        if item in tuple2:
            intersected.append(item)

    return tuple(intersected)

class SimplifiedCard:
    simple_converter_rank = {'Ace' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9, '10' : 10, 'Jack' : 11, 'Queen' : 12, 'King' : 13}
    simple_converter_suit = {'Spades' : 1, 'Hearts' : 2, 'Clubs' : 3, 'Diamonds' : 4}

    plays_possible = []

    def __init__(self, cards: card.CardGen):
        self.simple_cards = []

        for card in cards:
            self.simple_rank = self.simple_converter_rank[card.rank]
            self.simple_suit = self.simple_converter_suit[card.suit]

            self.simple_cards.append((self.simple_rank, self.simple_suit))

        self.simple_ranks = [rank for rank, suit in self.simple_cards]
        self.simple_suits = [suit for rank, suit in self.simple_cards]


        self.simple_cards_arranged_by_rank = list(sorted(self.simple_cards, key = lambda x: x[0]))

        self.plays = {
            "High Card" : [(1), [15, 1]],
            "Pair" : [(1, 1), [15, 2]],
            "Triple" : [(1, 1, 1) ,[15, 3]],
            "Mini Straight" : [(1, 2, 3), [35, 2]],
            "Impossible" : [(1, 1, 0, 1, 12), [50, 4]]
            }
    
    def play(self, play_name):

        self.cards_by_rank = [rank for rank, suit in self.simple_cards_arranged_by_rank]

        self.play_copy = self.plays[play_name][0]

        if play_name == "High Card":
            return True

        self.adder = 0
        while True:

            if intersection_tuples(tuple(rank + self.adder for rank in self.play_copy), self.cards_by_rank) == self.play_copy: #make more efficent one year
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
    print(simplified_hand.play_copy)
    print(simplified_hand.cards_by_rank)
    print(simplified_hand.adder)