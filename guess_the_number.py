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


def guess_number(goes, target):
    turns = 0

    while turns < goes:
        choice = int(input("Guess a number between 1 and 100\n"))
        turns += 1
        if choice == target:
            print(f"Congratulations you guessed the number in {turns} turns!")
            break
        elif choice < target:
            print("Your guess was too low")
        elif choice > target:
            print("Your guess was too high")

    if turns == goes and choice != target:
        print("Game over! You are out of turns")

def run_game():
    print("Welcome to number guesser!")
    target = random.randint(1, 100)
    print(target)
    goes = choose_level()
    guess_number(goes, target)


if __name__ == "__main__":
    run_game()
