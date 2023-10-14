import random
from art import logo

def calculate_score(cards):
  if len(cards) == 2 and sum(cards) == 21:
      return 0
  elif any(card == 11 for card in cards) and sum(player_cards) > 21:
      cards.remove(11)
      cards.append(1)
      return sum(cards)
  else:
      return sum(cards)

def compare_scores(player_total, dealer_total):
    if player_total == 0:
        print("You have won with a blackjack!")
    elif dealer_total == 0:
        print("The dealer has won with a blackjack!")
    elif player_total > dealer_total:
        print(f"You win! your total is {player_total} vs the dealer {dealer_total}")
    elif dealer_total > player_total:
        print(f"You have lost. The dealer has {dealer_total} vs your total of: {player_total}")
    else:
        print(f"It is a draw! You both have {player_total}")


def hit(cards):
    cards.append(random.choice(deck))
    return cards

def deal(player_cards, dealer_cards):
    game = [player_cards, dealer_cards]
    print("Dealing first card...")
    player_cards = hit(player_cards)
    dealer_cards = hit(dealer_cards)
    print(f"The dealer's hand is {dealer_cards} and their current score is {sum(dealer_cards)}")
    print(f"Your hand is {player_cards} and your current score is {sum(player_cards)}")
    print("Dealing second card...")
    player_cards = hit(player_cards)
    dealer_cards = hit(dealer_cards)
    print(f"The dealer's hand is {dealer_cards[0]} X")
    print(f"Your hand is {player_cards} and your current score is {sum(player_cards)}")
    return game

def play():
    print(logo)
    choice = input("Would you like to play blackjack? Type Y or N ").lower()
    if choice == "y":
        return True
    else:
        return False

while play():

    deck = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    player_cards = []
    dealer_cards = []
    player_total = 0
    dealer_total = 0
    game = deal(player_cards, dealer_cards)

    player_cards = game[0]
    dealer_cards = game[1]

    twist = True

    while twist:
        player_total = sum(player_cards)
        dealer_total = sum(dealer_cards)
        choice = input("Would you like another card? Type Y or N ").lower()
        if choice == "y":
            hit(player_cards)
            player_total = calculate_score(player_cards)
            print(f"The dealer's hand is {dealer_cards[0]} X")
            print(f"Your hand is {player_cards} and your current score is {player_total}")
            if player_total > 21:
                print("You have gone bust!")
                twist = False
            elif player_total == 0:
                print("You have won with a blackjack!")
                twist = False
        else:
            dealer_choice = random.choice([True, False])
            while sum(dealer_cards) < 21 and dealer_choice == True:
                print("dealer draws another")
                hit(dealer_cards)
                dealer_total = calculate_score(dealer_cards)
                dealer_choice = random.choice([True, False])
            print("Dealer stands")
            compare_scores(player_total, dealer_total)
            twist = False

    print("Game over")
