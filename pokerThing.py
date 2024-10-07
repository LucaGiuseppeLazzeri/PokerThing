import random
import time

# creating the arrays
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

#deck is created by comabing rank and suit, for every element in rank is combined with suits
deck = [(rank, suit) for rank in ranks for suit in suits]

# shuffle the cards in deck 
random.shuffle(deck)

# ask for player for ammount of players storing value as an int
players = int(input("How many players: "))

hands = {}


def dealTwoCards():
    global hands  # Ensure we're modifying the global hands dictionary
    hands.clear()  # Clear any existing hands
    for n in range(players):
        # hand is created by removing the top two elements of the deck array
        hand = [deck.pop() for _ in range(2)]
        # adds the player and their hand to the hands dictionary
        hands[n + 1] = hand  # Use integer keys for consistency

#a function to deal cards in middle
def dealCommunity():
    # deck has top elements remoived using pop the ammount of cards in determined by range(x)
    print("Flop: ", [deck.pop() for _ in range(3)])
    print("Turn: ", [deck.pop() for _ in range(1)])
    print("River: ", [deck.pop() for _ in range(1)])


#proof of stored and acessable hands
def showIndividualHands(chosenOne):
    
    #looking for the chosen hand in hands
    if chosenOne not in hands:
        print("Stop looking at my cards.")
        
    
    #finds chosen hand
    else:
        print(f"Player {chosenOne}: {hands[chosenOne]}")


def showAllHands():
    print("All players' hands:")
    for player, hand in hands.items():
        print(f"Player {player}: {hand}")



###########################################################################################

# Experimental code
           

    


###########################################################################################

# Test functions

def testingSIH():

    rangePlus1 = range(players, +1)

    for i in rangePlus1:
        showIndividualHands(i)

    print(rangePlus1)

###########################################################################################

print("Start")
dealTwoCards()
dealCommunity()

showAllHands()

him = int(input("Chose who to oversee: \n"))
showIndividualHands(him)

print("Finish")