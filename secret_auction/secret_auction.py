from colorama import init, deinit
import os
from art import logo

def clear_screen():
    init(autoreset=True)
    os.system("cls" if os.name == "nt" else "clear")
    deinit()

print(logo)

bidders = {}

def add_bidder():
  name = input("What is your name?\n")
  bid = int(input("What is your bid?\n"))
  bidders[name] = bid


def highest_bidder(bidders):
  highest_bid = 0
  winner = ""
  for person in bidders:
    if bidders[person] > highest_bid:
      highest_bid = bidders[person]
      winner = person
  print(f"The winner is {winner} with a bid of ${highest_bid}")


def print_bidders():
  decision = input("Are there any other bidders? Type 'yes' or 'no'\n")
  if decision == "no":
    highest_bidder(bidders)
  elif decision == "yes":
    clear_screen()
    add_bidder()
    print_bidders()


add_bidder()
print_bidders()
