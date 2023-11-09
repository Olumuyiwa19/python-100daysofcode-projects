import random
from hangman_wordly import word_collection
from hangman_gallery import logo, levels

# Choose a random word from the word_collection
hangman_word = random.choice(word_collection)
word_length = len(hangman_word)

# Initialize game variables
end_of_game = False
lives = 6

# Display the Hangman logo
print(logo)

#Testing code
print(f'Pssst, the solution is {hangman_word}.')

#Create blanks
display_word = ["_" for _ in range(word_length)]
display_word += "_"

# Main game loop
while not end_of_game:
    # Get user input for a letter guess
    guess_letter = input("Guess a letter: ").lower()

    # Check if the letter has already been guessed
    if guess_letter in display_word:
        print(f"You've already guessed {guess_letter}")

    #Check guessed letter
    for position in range(word_length):
        letter = hangman_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess_letter:
            display_word[position] = letter

    #Check if user is wrong.
    if guess_letter not in hangman_word:
        print(f"You guessed {guess_letter}, that's not in the word. You lose a life.")

        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display_word)}")

    #Check if user has got all letters.
    if "_" not in display_word:
        end_of_game = True
        print("You win.")

    # Display the current level of Hangman
    print(levels[lives])