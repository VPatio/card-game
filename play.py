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

        self.rank = 0
        self.suit = 0

        self.simple_cards_arranged_by_rank = list(sorted(self.simple_cards, key = lambda x: x[0]))

        self.plays = {
            "High Card" : [(), [15, 1]],
            "Pair" : [(0), [15, 2]],
            "Triple" : [(0, 0) ,[15, 3]],
            "Mini Straight" : [(1,1), [35, 2]],
            "Impossible" : [(4), [50, 4]]
            }
    
    def play(self, play_name):
        
        self.cards = self.simple_cards_arranged_by_rank

        self.cards_sorted = sorted(self.cards, key = lambda x: x[0])
        self.cards_sorted_only_rank = [rank for rank, suit in self.cards_sorted]

        if play_name == "Mini Straight":

            self.cards_sorted_only_rank = list(dict.fromkeys(self.cards_sorted_only_rank))

        self.difference_cards = difference_cards(self.cards_sorted_only_rank)
        

        if self.plays[play_name][0] in self.difference_cards:
            
            self.plays_possible.append(play_name)
            return play_name
        else:
            return "Not possible"


    # def eligible_plays(self):
    #     self.all_eligible_plays: list = []
        
    #     for simple_card_abr in self.simple_cards_arranged_by_rank:
    #         if simple_card_abr[0] > 0:
    #             self.simple_cards_arranged_by_rank = [(rank_abr - 1, suit_rememba) for rank_abr, suit_rememba in self.simple_cards_arranged_by_rank]
    #         elif simple_card_abr[0] == 0:
    #             pass

    #     for (rank_valid, amount_valid), (useless_chips, play_name) in zip(
    #         Counter(*self.plays.keys()).items(),
    #         self.plays.values()
    #         ):
    #         if self.simple_cards_arranged_by_rank
    #             self.all_eligible_plays.append(play_name)
    #     return self.all_eligible_plays
        


    

if __name__ == "__main__":
    hand = card.Deck().deck_52(return_result = True)

    simplified_hand = SimplifiedCard(hand)
    print(simplified_hand.play("High Card"))
    print(simplified_hand.difference_cards)
    print(simplified_hand.cards_sorted_only_rank)