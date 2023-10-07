import random

EASY = {"name": "Easy", "goes": 15}
MEDIUM = {"name": "Medium", "goes": 10}
HARD = {"name": "Hard", "goes": 5}

def choose_level():
    level = input("please choose your level: Easy, Medium, or Hard\n").lower()

    if level == "easy":
        return EASY["goes"]
    elif level == "medium":
        return MEDIUM["goes"]
    elif level == "hard":
        return HARD["goes"]
    else:
        print("You have not chosen a valid level. Please try again.")

    print(f"You've chosen the {level} level.")


def get_user_guess():
    while True:
        try:
           choice = int(input("Please choose a number between 1 and 100\n"))
           return choice
        except ValueError:
            print("Please enter a valid number")


def evaluate_guess(target, choice, turns):
    if choice == target:
        print(f"Congratulations! You guessed the number {target} correctly in {turns} turns")
        return True
    elif choice > target:
        print("Too high!")
        return False
    else:
        print("Too low!")
        return False

def run_game():
    print("Welcome to Number Guesser!")
    target = random.randint(1, 100)
    level = choose_level()
    print(f"You have {level} goes to guess the number")

    for turns in range(1, level + 1):
        choice = get_user_guess()
        if evaluate_guess(target, choice, turns):
            break
        else:
            print(f"You have {level - turns} goes left")
            print("Guess again!")

    if turns == level and choice != target:
        print(f"You are out of turns. The number was {target} Goodbye!")

if __name__ == "__main__":
    run_game()
