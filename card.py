import random


class CardGen:
    attributes = None

    border_check1: list[str] = ['2', '3', '4', '5', '6', '7', '8', '9', '10']
    border_check2: list[str] = ['Jack', 'Queen', 'King', 'Ace']
    border_check3: list[str] = ['blank']
    border_maker: dict[str, str] = {
        "1_left": "[",
        "1_right": "]",
        "2_left": "(",
        "2_right": ")",
        "3_left": "{",
        "3_right": "}"
    }

    def __init__(self, rank:str, suit:str):
        self.rank = rank
        self.suit = suit
        self.card_name = rank + " of " + suit

        if self.rank in self.border_check1:
            self.border_value: int = 1

        elif self.rank in self.border_check2:
            self.border_value: int = 2

        elif self.rank in self.border_check3:
            self.border_value: int = 3

        else:
            self.border_value: int = 0

    @property
    def border(self):
        self.bordered_card = self.border_maker[f"{self.border_value}_left"] + self.card_name + self.border_maker[f"{self.border_value}_right"]
        #for debugging purposes, don't listen to warning

        return self.bordered_card
    
    def __repr__(self):
        return self.card_name




class Deck:
#instead of always having to refer to self.deck you can go use return_result to instantly get that


    def __init__(self):
        self.rank_deck: int = 0
        self.suit_deck: int = 0
        self.rank_list_deck: list[str] = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        self.suit_list_deck: list[str] = ['Spades', 'Hearts', 'Clubs', 'Diamonds']


        self.deck: list = []
        self.copy_deck: list = []

    def deck_52(self, return_result: bool = False) -> list[CardGen]:
        self.deck = []
        self.copy_deck = []

        while True:
            self.deck.append(CardGen(self.rank_list_deck[self.rank_deck], self.suit_list_deck[self.suit_deck]))
            self.copy_deck.append(CardGen(self.rank_list_deck[self.rank_deck], self.suit_list_deck[self.suit_deck]))

            if self.rank_deck == 12:
                self.rank_deck = 0
                self.suit_deck += 1
            else:
                self.rank_deck += 1

            if self.suit_deck == 4:
                self.suit_deck = 0
                break
        
        if return_result == True:
            return self.deck

    def add_card(self, card_to_add: CardGen, return_result: bool = False):

        if card_to_add.rank not in self.rank_list_deck or card_to_add.suit not in self.suit_list_deck:
            raise Exception("Card not real")

        if isinstance(card_to_add, CardGen) == False:
            raise Exception("Not built with CardGen class")
        
        self.deck.append(card_to_add)
        self.copy_deck.append(card_to_add)
        #blueprint for adding card: Deck.add_card(CardGen("Rank", "Suit"))

        if return_result == True:
            return self.deck


    def make_hand(self, amount: int, return_result: bool = False):
        self.hand: list = []

        for _ in range(amount):
            self.hand.append(self.deck.pop(random.randint(0, len(self.deck) - 1)))

        if return_result == True:
            return self.hand

        #do I want to just return this or make as class variable? Class variable better because then I can make methods for it, but then do I make a new class for hand instead?? Just do class rn. I did sep class but in a completely different meaning yay
    
    def reset_deck(self, return_result: bool = False):
        self.deck = self.copy_deck.copy()

        self.hand: list = []

        if return_result == True:
            return self.deck

    #def __repr__(self):
    #    return ", ".join([card.card_name for card in self.deck])


if __name__ == "__main__":
    #print(deck := Deck().deck_52(return_result= True))
    #print(deck)

    deck2 = Deck()
    deck2.deck_52()
    deck2.add_card(CardGen(rank= "Jack", suit= "Hearts"))
    #print(deck2.deck)

    #print([card for card in deck.deck])

    #print(tuple(card for card in deck))
