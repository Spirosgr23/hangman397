# milestone_3.py

import random

# Define the function check_guess
def check_guess(guess):
    # Step 2: Convert the guess into lower case
    guess = guess.lower()

    # Step 3: Check if the guess is in the word
    if guess in secret_word:
        print(f"Good guess! {guess} is in the word.")
        return True
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")
        return False

# Define the function ask_for_input
def ask_for_input():
    while True:
        # Ask the user to guess a letter
        guess = input("Guess a letter: ")

        # Check that the guess is a single alphabetical character
        if len(guess) == 1 and guess.isalpha():
            # Call the check_guess function
            if check_guess(guess):
                break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

# Main program execution
word_list = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
secret_word = random.choice(word_list).lower() # Select a random word and make it lowercase

# Call the ask_for_input function
ask_for_input()
