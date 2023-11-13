### This project comprises of functions to encode and decode words for Ceasar Cipher program #####
from art import logo

def caesar_cipher(text, shift, direction):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    if direction == 'decode':
        shift = -shift  # Reverse the shift for decryption
    encrypted_text = ""
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + shift) % len(alphabet)
            encrypted_text += alphabet[new_position]
        else:
            encrypted_text += letter  # Keep non-alphabet characters unchanged
    return encrypted_text


print(logo)

replay = True
while replay:
    #get input from user about their choice encode or decode
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    #encrypt/decrypt the text
    result = caesar_cipher(text, shift, direction)
    print(f"The {direction}d text is: {result}")

    #allow user to continue or exit the program
    choice = input("Do you want to go again? Type 'yes' or 'no': ")
    if choice.lower() != 'yes':
        replay = False    #exit the loop if the user doesn't want to go again