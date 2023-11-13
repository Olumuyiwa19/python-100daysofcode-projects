### This project comprises of functions to encode and decode words for Ceasar Cipher program #####

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))


# def encrypt_word(plain_text, shift_amount):
#     encrypted_word = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         encrypted_word += new_letter
#     print(f" The encoded text is {encrypted_word}")

# def decrypt_word(encrypted_text, shift_amount):
#     decrypted_word = ""
#     for letter in encrypted_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         new_letter = alphabet[new_position]
#         decrypted_word += new_letter
#     print(f" The decoded text is {decrypted_word}")

# if direction == "encode":
#   encrypt_word(plain_text=text, shift_amount=shift)
# elif direction == "decode":
#   decrypt_word(encrypted_text=text, shift_amount=shift)


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

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

result = caesar_cipher(text, shift, direction)
print(f"The {direction}d text is: {result}")