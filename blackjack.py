logo = """
██████╗░██╗░░░░░░█████╗░░█████╗░██╗░░██╗░░░░░██╗░█████╗░░█████╗░██╗░░██╗
██╔══██╗██║░░░░░██╔══██╗██╔══██╗██║░██╔╝░░░░░██║██╔══██╗██╔══██╗██║░██╔╝
██████╦╝██║░░░░░███████║██║░░╚═╝█████═╝░░░░░░██║███████║██║░░╚═╝█████═╝░
██╔══██╗██║░░░░░██╔══██║██║░░██╗██╔═██╗░██╗░░██║██╔══██║██║░░██╗██╔═██╗░
██████╦╝███████╗██║░░██║╚█████╔╝██║░╚██╗╚█████╔╝██║░░██║╚█████╔╝██║░╚██╗
╚═════╝░╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝
"""
print(logo)
import random

def play_game():
    # Create a deck of cards
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11] * 4

    # Shuffle the deck
    random.shuffle(deck)

    # Deal two cards to the player and the dealer
    player_hand = []
    dealer_hand = []
    for i in range(2):
        player_hand.append(deck.pop())
        dealer_hand.append(deck.pop())

    # Player's turn
    while True:
        print("Your hand:", player_hand)
        print("Dealer's hand:", [dealer_hand[0], "X"])
        choice = input("Do you want to hit or stand? ")
        if choice == "hit":
            player_hand.append(deck.pop())
            if sum(player_hand) > 21:
                print("You busted!")
                return "dealer"
        else:
            break

    # Dealer's turn
    while sum(dealer_hand) < 17:
        dealer_hand.append(deck.pop())
    print("Your hand:", player_hand)
    print("Dealer's hand:", dealer_hand)
    if sum(dealer_hand) > 21:
        print("Dealer busted! You win!")
        return "player"
    elif sum(player_hand) > sum(dealer_hand):
        print("You win!")
        return "player"
    elif sum(dealer_hand) > sum(player_hand):
        print("Dealer wins!")
        return "dealer"
    else:
        print("It's a tie!")
        return "tie"

# Main game loop
while True:
    result = play_game()
    choice = input("Do you want to play again? (y/n) ")
    if choice.lower() != "y":
        break
