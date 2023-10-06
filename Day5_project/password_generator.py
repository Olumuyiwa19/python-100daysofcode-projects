#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Muyo-Password Generator!")
password_length = int(input("Enter the desired password length: "))
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


# Calculate the number of letters based on the remaining characters
nr_characters = password_length - nr_symbols - nr_numbers  # Assuming a fixed password length of 12 characters

# Check if there are enough characters for a valid password
if nr_characters < 0:
    print("Invalid input. The sum of symbols and numbers should not exceed the password length.")
else:
    # Define character sets for letters, symbols, and numbers
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    # Initialize the password as an empty list
    password = []

    # Generate letters for the password
    for letter in range(nr_letters):
        password.append(random.choice(letters))

    # Generate symbols for the password
    for symbol in range(nr_symbols):
        password.append(random.choice(symbols))

    # Generate numbers for the password
    for number in range(nr_numbers):
        password.append(random.choice(numbers))

    # Shuffle the password characters to make it random
    random.shuffle(password)

    # Convert the password list to a string
    generated_password = "".join(password)

    # Print the generated password
    print("Generated Password:", generated_password)
