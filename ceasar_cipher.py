alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(text,shift):
    #Todo-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
    #e.g.
    #plain_text = "hello"
    #shift = 5
    cipher_text = ""
    #print output: "The encoded text is mjqqt"
    for letter in text:
        position = alphabet.index(letter)
        new_position = position + shift
        # handle the case where the new_position is greater than 25 to wrap around to the beginning of the alphabet to avoid an out of bounds error
        if position + shift > 25:
            new_position = position + shift - 26

        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encoded text is {cipher_text}")

def decrypt(cipher_text,shift):
    text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift
        # handle the case where the new_position is greater than 25 to wrap around to the beginning of the alphabet to avoid an out of bounds error
        if position - shift < 0:
            new_position = position - shift + 26

        new_letter = alphabet[new_position]
        text += new_letter
    print(f"The decoded text is {text}")

def caesar(text,shift,direction):
    if direction == "encode":
        encrypt(text,shift)
    elif direction == "decode":
        decrypt(text,shift)
    else:
        print("Please enter a valid direction")

caesar(text,shift,direction)
