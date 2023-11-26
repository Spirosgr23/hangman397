# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

## Table of Contents
- [Project Description](#project-description)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [License](#license)
- [Use of Functions in Hangman](#use-of-functions-in-hangman)
- [Use of Object-Oriented Programming in Hangman](#use-of-object-oriented-programming-in-hangman)

## Project Description
This project is an implementation of the classic game Hangman. In this version, the computer selects a word at random from a predefined list of fruits, and the user attempts to guess it one letter at a time. This project serves not only as a fun and interactive game but also as an opportunity to learn and implement basic programming concepts in Python, including lists, user input handling, conditional statements, and the use of the `random` module.

## Installation
(Instructions on how to install and run the program will go here.)

## Usage
(Instructions on how to use the program, including any necessary commands or steps to start the game, will go here.)

## File Structure
- <file>.py: Main Python script containing the game logic.

  ## Use of Functions in Hangman

In the latest development phase of the Hangman game, we focused on enhancing code readability and maintainability by utilizing functions in Python. This approach allows us to break down complex processes into smaller, more manageable parts, making the code easier to understand and modify.

### Key Functions Implemented

- **`check_guess`**: This function takes the user's guessed letter as an argument, checks if it's present in the secret word, and returns a boolean value accordingly. It encapsulates the logic for validating the user's guess and provides feedback, significantly decluttering the main game loop.

- **`ask_for_input`**: Responsible for continuously prompting the user to guess a letter. It ensures the guess is a single alphabetical character and leverages the `check_guess` function to validate the guess against the secret word. By separating user input handling into its own function, we've made the code more organized and easier to follow.

These functions represent core components of our game's logic, demonstrating how breaking down code into smaller, reusable parts (functions) can enhance clarity and efficiency.

## Use of Object-Oriented Programming in Hangman

The Hangman game has evolved to incorporate more advanced features of Python, particularly object-oriented programming (OOP). We've encapsulated game logic within a class, enhancing code structure and maintainability.

### Class-Based Approach

- **`Hangman` Class**: Central to our game's architecture. It manages the game state and handles the logic for each turn of the game. Key attributes and methods include:
  - `__init__`: Initializes the game with a random word, sets the number of lives, and prepares the game state.
  - `check_guess`: This method processes the player's guess, updating the game state based on whether the guess is correct or incorrect.
  - `ask_for_input`: Manages user input, ensuring valid input and updating the list of guessed letters.

### Enhanced User Interaction

- **Guess Validation**: The game now handles invalid inputs more robustly, guiding the player to make valid guesses.
- **Repeated Guesses**: Players are informed if they attempt to guess a letter that they've already tried.

### Game Progression

- **Lives Management**: The game tracks the number of lives remaining, decrementing a life for incorrect guesses.
- **Feedback to Player**: After each guess, the game provides feedback, such as whether the guess was correct and how many lives remain.

This object-oriented approach allows for easier expansion and modification of the game in the future. Upcoming features could include more complex word lists, hints, or a graphical user interface.


## License
(Information about the license, if applicable, will go here.)
