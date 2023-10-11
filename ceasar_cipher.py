alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(text,shift,direction):
    result = ""
    for letter in text:
        position = alphabet.index(letter)
        if direction == "encode":
            new_position = position + shift
        else:
            new_position = position - shift
        # handle the case where the new_position is greater or less than 25 to wrap around to the beginning of the alphabet to avoid an out of bounds error
        if position + shift > 25:
            new_position = position + shift - 26
        elif position - shift < 0:
            new_position = position - shift + 26
        new_letter = alphabet[new_position]
        result += new_letter
    print(f"The text is {result}")

caesar(text,shift,direction)
