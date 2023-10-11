import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
non_alphabet = [' ', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', '|', '\\', ';', ':', '\'', '"', ',', '.', '<', '>', '/', '?', '`', '~', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
print(art.logo)

def run_game(play="yes"):
    while play == "yes":
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(text,shift,direction)
        play = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")


def caesar(text,shift,direction):

        result = ""
        if direction == "decode":
            shift *= -1
            print(shift)
        for letter in text:
            if letter in non_alphabet:
                result += letter
                continue
            position = alphabet.index(letter)
            new_position = position + shift
            if new_position > 25 or new_position < 0:
                new_position = new_position % 25
            new_letter = alphabet[new_position]
            result += new_letter
        print(f"The text is {result}")

run_game()
