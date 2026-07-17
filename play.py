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

        self.simple_ranks = [rank for rank, suit in self.simple_cards]
        self.simple_suits = [suit for rank, suit in self.simple_cards]

        self.rank = 0
        self.suit = 0

        self.simple_cards_arranged_by_rank = list(sorted(self.simple_cards, key = lambda x: x[0]))

        self.plays = {
            (0) : [[15, 1], "High Card"],
            (0, 0) : [[15, 2], "Pair"],
            (0, 0, 0) : [[15, 3], "Triple"],
            (0, 1, 2) : [[35, 2], "Mini Straight"],
            (0, 0, 0, 0, 0) : [[50, 4], "Impossible"]
            }
        
    def eligible_plays(self):
        self.all_eligible_plays: list = []
        
        for simple_card_abr in self.simple_cards_arranged_by_rank:
            if simple_card_abr[0] > 0:
                self.simple_cards_arranged_by_rank = [(rank_abr - 1, suit_rememba) for rank_abr, suit_rememba in self.simple_cards_arranged_by_rank]
                    #find new way to do this without having to do for in loops (thank you python for not making me have to do 9000 nested loops)
            elif simple_card_abr[0] == 0:
                pass
            
            self.counter_at_home = 0
            
            for simple_card_abr3 in self.simple_cards_arranged_by_rank:
                if self.simple_cards_arranged_by_rank[0] == simple_card_abr3:
                    self.rank_to_match = simple_card_abr3[0]
                
                elif simple_card_abr3[0] != self.rank_to_match:
                    break
                else:
                    self.counter_at_home +=1

            for (card_valid, amount_valid), (useless_chips, play_name) in zip(
                Counter(self.plays.keys()).items(),
                self.plays.values()
                ):
                if self.counter_at_home >= amount_valid:
                    self.all_eligible_plays.append(play_name)
        return self.all_eligible_plays
        


    

if __name__ == "__main__":
    hand = card.Deck().deck_52(return_result = True)

    simplified_hand = SimplifiedCard(hand)
    print(simplified_hand.eligible_plays())