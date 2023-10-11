import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(text,shift,direction):
    result = ""
    if direction == "decode":
        shift *= -1
        print(shift)
    for letter in text:
        position = alphabet.index(letter)
        new_position = position + shift
        if new_position > 25 or new_position < 0:
            new_position = new_position % 25
        new_letter = alphabet[new_position]
        result += new_letter
    print(f"The text is {result}")

caesar(text,shift,direction)
