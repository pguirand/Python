import time
from random import shuffle
from random import Random 



# WAR GAME CARD
start_time = time.time()

SUITE = 'H S D C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

# print(SUITE)
# print(RANKS)

# mycards = []
# for r in RANKS:
#     for s in SUITE:
#         mycards.append((s,r))

# -----------------
#  OU PLUS SIMPLE 
# -----------------

#mycards = [(s,r) for s in SUITE for r in RANKS]

# INSERT LINE ABOVE IN CLASS INSTEAD

#print(mycards)
#print(f"{time.time() - start_time} secondes")

class Deck():
    '''
    This object will create a deck of cards to 
    initiate play. You can this Deck list of 
    cards to split in half and give to the players.
    It will use SUITE and RANKS to create the deck.
    it should also have a method for splitting/
    cutting the deck in half and shuffling the deck.

    '''
    def __init__(self):
        print("Creating New ordered Deck...")
        self.allcards = [(s,r) for s in SUITE for r in RANKS]

    def shuffle(self):
        print("SHUFFLING DECK")
        shuffle(self.allcards)

    def split_in_half(self):
        print("SPLITTING")
        return (self.allcards[:26],self.allcards[26:])

# game = Deck()
# game.shuffle()
# game.split_in_half()

# x = game.split_in_half()
# print(x)

    # for i in x[0]:
    #     print(f"{i}\n")

class Hand:
    '''
    Hand class. Each player has a hand, and can add or 
    remove cards from that hand. There should be add
    and remove card method.

    '''
    def __init__(self,cards):
        self.cards = cards

    def __str__(self):
        return f"Contains {len(self.cards)} cards"

    def add(self,added_cards):
        self.cards.extend(added_cards)
    
    def remove_card(self):
        return self.cards.pop()

class Player:
    """
    this is the player class, which takes in a name and 
    an instance of a Hand class object. The player
    can then play cards and check if they still have cards
    
    """

    def __init__(self, name,hand):
        self.name = name
        self.hand = hand
    
    def play_card(self):
        drawn_card = self.hand.remove_card()
        print(f"{self.name} has placed {drawn_card}")
        print("\n")
        return drawn_card

    def remove_war_cards(self):
        war_cards = []
        if len(self.hand.cards) < 3:
            return self.hand.cards
        else:
            for x in range(3):
                war_cards.append(self.hand.cards.pop())
            return war_cards

    def still_has_cards(self):
        """
        Return True if player still has cards left
        """
        return len(self.hand.cards)



print("Welcome to war, let's begin...")

#Create new Deck and split in half:
d = Deck()
d.shuffle()
half1,half2 = d.split_in_half()

#Create both players
comp = Player("computer",Hand(half1))

name = input("what is your name ?")
user = Player(name,Hand(half2))


total_rounds = 0
war_count = 0

while user.still_has_cards and comp.still_has_cards():
    total_rounds += 1
    print("Time for a new round")
    print("here are the current standings")
    print(f"{user.name} has the count {str(len(user.hand.cards))}")
    print(f"{comp.name} has the count {str(len(comp.hand.cards))}")
    print("Play a card !")
    print("\n")

    table_cards = []

    c_card = comp.play_card()
    p_card = user.play_card()

    table_cards.append(c_card)
    table_cards.append(p_card)

    if c_card[1] == p_card[1]:
        war_count += 1

        print("war !")
        table_cards.extend(user.remove_war_cards())
        table_cards.extend(comp.remove_war_cards())

        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)
    else:        
        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)

print(f"GAME OVER, number of rounds : {str(total_rounds)}")
print(f"a war happened {str(war_count)} times")



# A suivre....



























