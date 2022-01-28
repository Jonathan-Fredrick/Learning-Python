import random

suits = ("Hearts", "Diamonds", "Spades", "Clubs")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10,
          "Jack": 10,
          "Queen": 10, "King": 10, "Ace": 11}

playing = True


class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ""
        for card in self.deck:
            deck_comp += "\n" + card.__str__()
        return "The deck has: " + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card


class Hand:
    def __init__(self):
        self.card = []
        self.value = 0
        self.ace = 0

    def add_card(self, card):
        self.card.append(card)  # this would be used with deck.deal
        self.value += values[card.rank]

        if card.rank == "Ace":
            self.ace += 1

    def adjust_for_aces(self):
        while self.value > 21 and self.ace:  # zero returns a false boolean value
            self.value -= 10
            self.ace -= 1







class Chips:
    def __init__(self, total=100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


# functions to play the game

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("How many chips do you like to bet"))
        except:
            print("Sorry please provide an integer")
        else:
            if chips.bet > chips.total:
                print("Sorry you do not have enough chips, you currently have: {} chips left".format(chips.total))
            else:
                break


def hit(deck, hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_aces()


def hit_or_stand(deck, hand):
    global playing  # to control an upcoming while loop
    while True:
        x = input('Hit or Stand? Enter h or s ')

        if x[0].lower() == 'h':
            hit(deck,hand)
        elif x[0].lower() == 's':
            print('Player Stands, Dealers turn')
        else:
            print("Sorry i did not understand that, please enter 'h' or 's' only")

        break

# next are functions that handle each of the game situation if its going to end

def player_busts(player, dealer,chips):
    print("BUST PLAYER")
    chips.lose_bet()
def player_wins(player, dealer,chips):
    print("PLAYER WINS")
    chips.win_bet()
def dealer_busts(player, dealer,chips):
    print("PLAYER WINS, DEALER BUSTED")
    chips.win_bet()
def dealer_wins(player, dealer,chips):
    print("DEALER WINS")
    chips.lose_bet()
def push(player, dealer,chips):
    print("Dealer and Player tie! PUSH")

## AND NOW THE GAME
while True:
    print("Welcome to BLACKJACK")
    # create and shuffle deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # set up players chips
    player_chips = Chips()

    # prompt player for their bet
    take_bet(player_chips)
    # show cards vut keep one dealer card hidden
    #show_some(player_hand, dealer_hand)

    while playing:
        # prompt for player to hit or stand
        hit_or_stand(deck, player_hand)
        # show cards vut keep one dealer card hidden
        #show_some(player_hand,dealer_hand)

        # if player's hand exceed 21, run player bust and breakout of the loop
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)

            break

    # if player hasn't busted, play Dealer's hand until dealer reaches 17
    if player_hand.value < 21:

        while dealer_hand.value < 17:
            hit(deck,dealer_hand)

        # show all cards
       # show_all(player_hand,dealer_hand)

        # run different winning scenarios
        if dealer_hand.value > 21:
            daeler_busts(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
        else:
            push(player_hand, dealer_hand, player_chips)

    # inform player of their chips total
    print("\n Player total chips are at {}".format(player_chips.total))

    # ask to play again
    new_game = input("Would you like to play another hand? y/n")
    if new_game[o].lower() == 'y':
        playing = True
    else:
        print("Thank you for playing")
        break











# Testing
test_deck = Deck()
test_deck.shuffle()
# print(test_deck)

test_player = Hand()
pulled_card = test_deck.deal()
print(pulled_card)
test_player.add_card(pulled_card)
print(test_player.value)
# shorter method to return only the value
print(test_player.value)
